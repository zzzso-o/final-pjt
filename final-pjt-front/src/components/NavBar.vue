<template>
  <div class="container">
    <b-navbar>
      <template #brand>

      </template>
      <template #start>
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          <img src="@/assets/meta.png" >
        </b-navbar-item>
        <!-- <b-navbar-item>
          <router-link :to="{ name: 'home' }"><strong>Home</strong></router-link>
        </b-navbar-item> -->
        <b-navbar-item>
          <router-link :to="{ name: 'movies' }"><strong>Popular Movies</strong></router-link>
        </b-navbar-item>
        <b-navbar-item>
          <router-link :to="{ name: 'articles' }"><strong>Community</strong></router-link>
        </b-navbar-item>

        </template>
      
        <template #end>
        <b-navbar-item tag="div" v-if="!isLoggedIn">
          <router-link :to="{ name: 'login' }" ><strong>Login</strong></router-link>
        </b-navbar-item>
        <b-navbar-item v-if="!isLoggedIn">
          <router-link :to="{ name: 'signup' }"><strong>Signup</strong></router-link>
        </b-navbar-item>
        <b-navbar-item v-if="isLoggedIn">
          <router-link :to="{ name: 'mymovie', params: { username } }" class="is-primary"><strong>MyMovie</strong></router-link>
        </b-navbar-item>
        <b-navbar-item v-if="isLoggedIn">
          <router-link :to="{ name: 'logout' }" ><strong>Logout</strong></router-link>
        </b-navbar-item>
        </template>
    </b-navbar>
  </div>
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
