<template>
  <div>
    <h1>Logout</h1>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    data() {
      return {
          
      }
    },
    methods: {
      ...mapActions(['logout']),

    },
    computed: {
      ...mapGetters(['isLoggedIn'])
    },
    created() {
      if (this.isLoggedIn) {
        this.logout()
      } else {
        alert('이미 로그아웃')
        this.$router.back()
      }
    },
    
  }
</script>

<style></style>
