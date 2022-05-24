<template>
  <div class="container">
    
    <h1 class=title>Login</h1>
    
    <account-error-list v-if="authError"></account-error-list>
    
    <div class="logincontainer box">
      <form @submit.prevent="login(credentials)">
        <div class="field">
          <p class="control has-icons-left">
            <b-input placeholder="Enter your username" v-model="credentials.username" id="username"
                icon="account">
            </b-input>
            <span class="icon is-small is-left">
              <i class="fa fa-user"></i>
            </span>
          </p>
        </div>
        <div class="field">
          <p class="control has-icons-left">
            <b-input type="password" v-model="credentials.password" id="password"
              placeholder="Enter your password"
              password-reveal>
            </b-input>
            <span class="icon is-small is-left">
              <i class="fa fa-key"></i>
            </span>
          </p>
        </div>
        <br>
        <button class="button is-fullwidth">로그인</button>
      </form>
    </div>


  </div>
</template>

<script>

  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
		...mapGetters(['authError'])
	},
	methods: {
		...mapActions(['login'])
	},
  }
</script>

<style>  
  .container {
    width: 750px;
  }
  .logincontainer {
    width: 450px;
    margin: auto;
  }
</style>
