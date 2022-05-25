<template>
  <div class="home">
    <now-movie>

    </now-movie>
    

  </div>
</template>

<script>
// @ is an alias to /src
// import searchMovies from '../components/SearchBar.vue'
import NowMovie from '../components/NowMovie.vue'
import { mapState } from 'vuex'

export default {
  name: 'HomeView',
  components: {
    NowMovie,
    // searchMovies
  },
  computed: {
    ...mapState(['nowMovies'])
  },
}
</script>
