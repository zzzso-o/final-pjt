<template>
  <div>


    <div class="container">
      
      <div class="logincontainer box">
        <div class="imgcontainer">
          <img src="@/assets/meta.png">
        </div>
        <br>
        <p class="text-center content is-small">회원가입 후 더 다양한 서비스를 즐겨보세요 !</p>
        <account-error-list v-if="authError"></account-error-list>
        <br>
        <form @submit.prevent="signup(credentials)">
          <div class="field">
            <p class="control has-icons-left">
              <b-input placeholder="Enter your username" v-model="credentials.username" id="username">
              </b-input>
              <span class="icon is-small is-left">
                <i class="fa fa-user"></i>
              </span>
            </p>
          </div>
          <div class="field">
            <p class="control has-icons-left">
              <b-input type="password" v-model="credentials.password1" id="password1"
                placeholder="Enter your password"
                password-reveal>
              </b-input>
              <span class="icon is-small is-left">
                <i class="fa fa-key"></i>
              </span>
            </p>
          </div>
          <div class="field">
            <p class="control has-icons-left">
              <b-input type="password" v-model="credentials.password2" id="password2"
                placeholder="Enter your password"
                password-reveal>
              </b-input>
              <span class="icon is-small is-left">
                <i class="fa fa-key"></i>
              </span>
            </p>
          </div>
          <br>
          <button class="button is-fullwidth">가입하기</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
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

