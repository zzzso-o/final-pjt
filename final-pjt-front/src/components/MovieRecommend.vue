

<template>
  <div>
      <h1 class='title'>이번달 추천영화</h1>
      <div 
      v-for="movie in recommendmovie" :key="movie.id">
      {{ movie.title}}
      </div>


  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  const now = new Date();
  const month = now.getMonth();

export default {
  data() {
    return {
      recommendmovie: [],
      reco : ['hi']
    }
  },
  methods:{
    ...mapActions(['fetchPopularMovies']),
    getMovieMonth(){
      
    for (const movie of this.$store.getters.popularMovies){
      const movie_month_temp = movie.release_date.substr(5,2)
      const movie_month = movie_month_temp.replace(/(^0+)/, "")
      if (movie_month == month){
        this.recommendmovie.push(movie)
      }
    }
    },
	},
  computed: {
    ...mapGetters(['popularMovies']),
    // ...mapState(['popularMovies']),

    },
    created(){
      this.fetchPopularMovies()
      this.getMovieMonth()
    }
}

</script>

<style>

</style>