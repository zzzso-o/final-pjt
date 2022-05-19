import Vue from 'vue'
import Vuex from 'vuex'

import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

import articles from './modules/articles'
import accounts from './modules/accounts'
import movies from './modules/movies'
import mymovie from './modules/mymovie'


Vue.use(Vuex)
Vue.use(Buefy)

export default new Vuex.Store({
  modules: { accounts, articles, movies, mymovie},
})
