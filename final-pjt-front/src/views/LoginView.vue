<template>
  <div class="container">
    
    <div class="logincontainer box">
      <div class="imgcontainer">
        <img src="@/assets/meta.png">
      </div>
      <br>
      <p class="text-center content is-small">로그인 후 더 다양한 서비스를 즐겨보세요 !</p>
      <account-error-list v-if="authError"></account-error-list>
      <br>
      <form @submit.prevent="login(credentials)">
        <div class="field">
          <p class="control has-icons-left">
            <b-input placeholder="Enter your username" v-model="credentials.username" id="username">
            </b-input>
            <span class="icon is-small is-left">
              <i class="fas fa-user"></i>
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
              <i class="fas fa-lock"></i>
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
  .imgcontainer{
    width: 225px;
    margin: auto;
    padding: 70px;
    padding-bottom : 10px;
  }

</style>
