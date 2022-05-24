<template>
  <div class="container">
    <h1 class=title>Login</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="login(credentials)" class ="box c"  >
      <section class="">
      <b-field label="ID" type="is-success" 

      message="The ID is available"  >
        <input v-model="credentials.username" 
        placeholder="enter your ID" id="username" required />
      </b-field>

      <b-field label="PW" type="is-success" 
      message="The password is available" >
        <input v-model="credentials.password" type="password" 
        placeholder="enter your PW"  id="password" required password-reveral />
      </b-field>
      
      <div class = "buttons">
      <b-button type="is-primary" > Login </b-button>
      </div>
      </section>
    </form>
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




</style>
