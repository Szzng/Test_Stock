import axios from 'axios'
// axios.defaults.xsrfCookieName = 'csrftoken'
// axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const userStore = {
  namespaced: true,
  state: {
    dialog: {
      register: false,
      login: false
    },
    registerState: {
      isRegister: false,
      isRegisterError: false
    },
    loginState: {
      isLogin: false,
      isLoginError: false
    },
    me: {
      username: 'Guest'
    }
  },
  mutations: {
    dialogOpen (state, kind) {
      console.log('dialogOpen', kind)
      if (kind === 'register') {
        state.dialog.register = true
      } else if (kind === 'login') {
        state.dialog.login = true
      }
    },
    registerSuccess (state, userInfo) {
      state.registerState.isRegister = true
      state.registerState.isRegisterError = false
      state.dialog.register = false
      state.dialog.login = true
    },
    loginSuccess (state, userInfo) {
      state.loginState.isLogin = true
      state.loginState.isLoginError = false
      state.me.username = userInfo.username
      state.dialog.login = false
    },
    logoutSuccess (state) {
      state.loginState.isLogin = false
      state.loginState.isLoginError = false
      state.me.username = 'Guest'
    }
  },
  actions: {
    register ({ dispatch }, postData) {
      console.log('register()...')
      axios
        .post('api/accounts/registrater/', postData)
        .then(res => {
          console.log('Register POST res', res)
          dispatch('login')
        })
        .catch(err => {
          console.log('Register POST err', err.response)
          alert('Register NOK')
        })
    },
    login ({ dispatch }, postData) {
      console.log('login()...')
      axios
        .post('api/accounts/login/', postData)
        .then(res => {
          console.log('Login1 POST res', res)
          let accessToken = res.data.access_token
          localStorage.setItem('access_token', accessToken)
          dispatch('getUserInfo')
        })
        .catch(err => {
          console.log('Login1 POST err', err.response)
          alert('login NOK')
        })
    },
    getUserInfo ({ commit }) {
      console.log('getUserInfo()...')
      let config = {
        headers: {
          'access-token': localStorage.getItem('access_token')
        }
      }
      axios
        .get('', config)
        .then(response => {
          console.log('Login2 GET res', response)
          let userInfo = response.data
          commit('loginSuccess', userInfo)
        })
        .catch(error => {
          console.log('Login2 GET err', error.response)
          alert('login NOK')
        })
    },
    logout ({state, commit}) {
      console.log('logout()...')
      //   axios
      //     .get('/accounts/logout/')
      //     .then(res => {
      //       console.log('Logout GET res', res)
      localStorage.removeItem('access_token')
      alert(`${state.me.username}님이 로그아웃 하셨습니다.`)
      commit('logoutSuccess')
      // })
      // .catch(err => {
      //   console.log('Logout GET err.response', err.response)
      //   alert('logout NOK')
      // })
    }
  }
}

export default userStore
