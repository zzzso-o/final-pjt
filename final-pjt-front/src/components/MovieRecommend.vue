

<template>
  <div>
    <div class="container">
      <h1 class="title">RECOMMEND MOVIES</h1>
      <div class="row">
        <div v-for="movie in popularMovies" :key="movie.id" class="card col-3">
          <div class="card-image">
            <figure class="image">
              <router-link :to="{ name: 'movie', params: {movieId: movie.pk} }">
                <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="movie poster" class=" is-128x128">
              </router-link>
            </figure>
          </div>
          <div class="content">
            <div class="media">
              <p><strong>{{ movie.title }}</strong>
                ({{ movie.release_date.substr(0,4) }})
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    



  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  // const now = new Date();
  // const month = now.getMonth();

export default {
  data() {
    return {
      recommendmovie: [],
      reco : ['hi'],
      username: this.$route.params.username,
    }
  },
  methods:{
    ...mapActions(['fetchPopularMovies']),
    // getMovieMonth(){
    // for (const movie of this.popularMovies){
    //   const movie_month_temp = movie.release_date.substr(5,2)
    //   const movie_month = movie_month_temp.replace(/(^0+)/, "")
    //   if (movie_month == month){
    //     this.recommendmovie.push(movie)
    //   }
    // }
    // },
	},
  computed: {
  ...mapGetters(['popularMovies']),
  // ...mapState(['popularMovies']),
  },
  created(){
    this.fetchPopularMovies()
    // this.getMovieMonth()
  }
}

</script>

<style>

</style>