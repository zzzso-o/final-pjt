import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
    // state는 직접 접근
    state: {
      token: localStorage.getItem('token') || '' ,
      currentUser: {},
      profile: {},
      authError: null,
    },
    // state는 getters 를 통해서 접근
    getters: {
      isLoggedIn: state => !!state.token, // 토큰이 있을경우 isLoggedIn
      currentUser: state => state.currentUser,
      profile: state => state.profile,
      authError: state => state.authError,
      authHeader: state => ({ Authorization: `Token ${state.token}`})
    },
    
    mutations: {
      SET_TOKEN: (state, token) => state.token = token,
      SET_CURRENT_USER: (state, user) => state.currentUser = user,
      SET_PROFILE: (state, profile) => state.profile = profile,
      SET_AUTH_ERROR: (state, error) => state.authError = error
    },
  
    actions: {
      saveToken({ commit }, token) {
        commit('SET_TOKEN', token) // commit으로 mutations에 접근 , state에 token 추가 
        localStorage.setItem('token', token) // localStorage에 token 추가
      },
  
      removeToken({ commit }) {
        commit('SET_TOKEN', '') // commit으로 mutations에 접근 , state에 token 삭제 
        localStorage.setItem('token', '') // localStorage에 token 삭제
      },

      login({ commit, dispatch }, credentials) {
        axios({
          url: drf.accounts.login(),
          method: 'post',
          data: credentials
        })
          .then(res => {
            const token = res.data.key
            dispatch('saveToken', token)
            dispatch('fetchCurrentUser')
            router.push({ name: 'home' })
          })
          .catch(err => {
            console.error(err.response.data)
            commit('SET_AUTH_ERROR', err.response.data)
          })
      },
  
      signup({ commit, dispatch }, credentials) {
        axios({
          url: drf.accounts.signup(),
          method: 'post',
          data: credentials
        })
          .then(res => {
            const token = res.data.key
            dispatch('saveToken', token)
            dispatch('fetchCurrentUser')
            router.push({ name: 'home' })
          })
          .catch(err => {
            console.error(err.response.data)
            commit('SET_AUTH_ERROR', err.response.data)
          })
      },
  
      logout({ getters, dispatch }) {
        axios({
          url: drf.accounts.logout(),
          method: 'post',
          data: {},
          headers: getters.authHeader,
        })
          .then(() => {
            .dispatch('removeToken')
            // alert('성공적으로 logout!')
            router.push({ name: 'login' })
          })
          .error(err => {
            console.error(err.response)
          })
      },

  
      fetchCurrentUser({ commit, getters, dispatch }) {
        if (getters.isLoggedIn) { // 이미 사용자가 로그인 했다면, 토큰이 있다면 
          axios({
            url: drf.accounts.currentUserInfo(),
            method: 'get',
            headers: getters.authHeader,
          })
            .then(res => commit('SET_CURRENT_USER', res.data))
            .catch(err => {
              if (err.response.status === 401) {
                dispatch('removeToken')
                router.push({ name: 'login' })
              }
            })
        }
      },

    },
  }
  