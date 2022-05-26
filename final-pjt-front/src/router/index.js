import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'

import ArticleListView from '@/views/ArticleListView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleNewView from '@/views/ArticleNewView'
import ArticleEditView from '@/views/ArticleEditView'


import MyMovieView from '@/views/MyMovieView.vue'
import MyArticlesView from '@/views/MyArticlesView.vue'
import MyCommentsView from '@/views/MyCommentsView.vue'
import MyUserScoreView from '@/views/MyUserScoreView.vue'

import PopularMovieListView from '@/views/PopularMovieListView.vue'
import PopularMovieDetailView from '@/views/PopularMovieDetailView.vue'


Vue.use(VueRouter)



const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },

  {
    path: '/articles',
    name: 'articles',
    component: ArticleListView
  },
  {
    path: '/articles/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/articles/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },

  {
    path: '/articles/:articlePk',
    name: 'article',
    component: ArticleDetailView
  },

  {
    path: '/mymovie/:username',
    name: 'mymovie',
    component: MyMovieView
  },
  {
    path: '/mymovie/myarticles/:username',
    name: 'myarticles',
    component: MyArticlesView
  },
  {
    path: '/mymovie/mycomments/:username',
    name: 'mycomments',
    component: MyCommentsView
  },
  {
    path: '/mymovie/myuserscore/:username',
    name: 'myuserscore',
    component: MyUserScoreView
  },

  {
    path: '/movies',
    name: 'movies',
    component: PopularMovieListView
  },
  {
    path: '/movies/:movieId',
    name: 'movie',
    component: PopularMovieDetailView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  // 이전 페이지에서 발생한 에러메시지 삭제
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup']

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('Require Login. Redirecting..')
    next({ name: 'login' })
  } else {
    next()
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'articles' })
  }
})



export default router
