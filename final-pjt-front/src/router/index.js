import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store'

import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'

import ArticleListView from '@/views/ArticleListView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'

import MyMovieView from '@/views/MyMovieView.vue'
import MyMovieRecommendView from '@/views/MyMovieRecommendView.vue'
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
    path: '/signup',
    name: 'signup',
    component: SignupView
  },

  {
    path: '/community',
    name: 'community',
    component: ArticleListView
  },
  {
    path: '/community/:articlePk',
    name: 'article',
    component: ArticleDetailView
  },

  {
    path: '/mymovie/:username',
    name: 'mymovie',
    component: MyMovieView
  },
  {
    path: '/mymovie/recommend/:username',
    name: 'myrecommend',
    component: MyMovieRecommendView 
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
    path: '/popular',
    name: 'movies',
    component: PopularMovieListView
  },
  {
    path: '/popular/:moviePk',
    name: 'movie',
    component: PopularMovieDetailView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router