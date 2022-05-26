<template>
  <div class="container">
    <movie-recommend></movie-recommend>
    <h2>{{ currentUser.username }}님을 위한 추천영화 !</h2>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import MovieRecommend from '../components/MovieRecommend.vue'

export default {
  components:{
    MovieRecommend
  },
  computed:{
    ...mapGetters(['currentUser']),
  },

}
</script>

<style>

</style>