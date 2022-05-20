<template>
  <b-navbar>
    <template #brand>
    <b-navbar-item tag="router-link" :to="{ path: '/' }">
      <img
          src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
          alt="Lightweight UI components for Vue.js based on Bulma"
      >
    </b-navbar-item>
    </template>
    <template #start>
      <b-navbar-item>
        <router-link :to="{ name: 'home' }"><strong>Home</strong></router-link>
      </b-navbar-item>
      <b-navbar-item>
        <router-link :to="{ name: 'movies' }">Popular Movies</router-link>
      </b-navbar-item>
			<b-navbar-item>
        <router-link :to="{ name: 'articles' }">Community</router-link>
      </b-navbar-item>
      <b-navbar-item>
        <router-link :to="{ name: 'mymovie', params: { username } }">MyMovie</router-link>
      </b-navbar-item>
      </template>

      

      <template #end>
      <b-navbar-item tag="div">
      <div class="buttons">


      <!-- <b-navbar-item tag="div" v-if="!isLoggedIn"> -->
        <router-link :to="{ name: 'login' }" class="button is-primary"><strong>Login</strong></router-link>
      <!-- </b-navbar-item> -->
      <!-- <b-navbar-item v-if="!isLoggedIn"> -->
        <router-link :to="{ name: 'signup' }" class="button is-light">Signup</router-link>
      <!-- </b-navbar-item> -->

      </div>
      </b-navbar-item>

      <b-navbar-item v-if="isLoggedIn">
        <router-link :to="{ name: 'mymovie', params: { username } }">MyMovie</router-link>
      </b-navbar-item>
      <b-navbar-item v-if="isLoggedIn">
        <router-link :to="{ name: 'logout' }">Logout</router-link>
      </b-navbar-item>

      </template>
  </b-navbar>
</template>

<script>


  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style></style>
