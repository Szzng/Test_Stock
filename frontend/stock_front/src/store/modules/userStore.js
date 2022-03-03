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
      if (kind === 'login') {
        state.dialog.login = true
      } else if (kind === 'register') {
        state.dialog.register = true
      }
    },
    loginSuccess (state, userInfo) {
      state.loginState.isLogin = true
      state.loginState.isLoginError = false
      state.me.username = 'sz'
      state.dialog.login = false
    },
    logoutSuccess (state) {
      state.loginState.isLogin = false
      state.loginState.isLoginError = false
      state.me.username = 'Guest'
    }
  },
  actions: {
    login ({ dispatch }, postData) {
      console.log('login()...')
      axios
        .post('/accounts/login/', postData)
        .then(res => {
          console.log('Login1 POST res', res)
          let token = res.data.token
          localStorage.setItem('access_token', token)
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
