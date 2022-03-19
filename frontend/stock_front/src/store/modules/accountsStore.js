import axios from 'axios'
// axios.defaults.xsrfCookieName = 'csrftoken'
// axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const accountsStore = {
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
      axios
        .post('api/accounts/register/', postData)
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
      axios
        .post('api/accounts/login/', postData)
        .then(res => {
          console.log('Login POST res', res)
          let accessToken = res.data.access_token
          let refreshToken = res.data.refresh_token
          localStorage.setItem('access_token', accessToken)
          localStorage.setItem('refresh_token', refreshToken)
          dispatch('getUserInfo')
        })
        .catch(err => {
          console.log('Login POST err', err.response)
          alert('login NOK')
        })
    },
    getUserInfo ({ commit }) {
      if (localStorage.getItem('access_token')) {
        let config = {
          headers: {
            'access-token': localStorage.getItem('access_token')
          }
        }
        axios
          .get('api/accounts/user/', config)
          .then(response => {
            console.log('getUserInfo GET res', response)
            let userInfo = response.data
            commit('loginSuccess', userInfo)
          })
          .catch(error => {
            console.log('getUserInfo GET err', error.response)
          })
      }
    },
    logout ({state, commit}) {
      axios
        .post('api/accounts/logout/', {'refresh': localStorage.getItem('refresh_token')})
        .then(res => {
          console.log('Logout POST res', res)
          localStorage.removeItem('access_token')
          alert(`${state.me.username}님이 로그아웃 하셨습니다.`)
          commit('logoutSuccess')
        })
        .catch(err => {
          console.log('Logout POST err.response', err.response)
          alert('logout NOK')
        })
    }
  }
}

export default accountsStore
