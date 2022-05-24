<template>
  <div class="container">
    {{ currentUser.pk }}dd
    <movie-recommend></movie-recommend>
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