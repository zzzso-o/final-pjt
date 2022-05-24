<template>
  <div>
    <h1>Movie Detail</h1>
    {{ popularMovie.homepage }}
    {{ popularMovie.adult }}
    {{ popularMovie.genres }}
    {{ popularMovie.title }}
    {{ popularMovie.overview }}
    {{ popularMovie.release_date }}
    {{ popularMovie.vote_average }}
    {{ popularMovie.poster_path}}
    <div class="container">
      <div class="card-image">
        <figure class="image">
          <img :src="`https://image.tmdb.org/t/p/w500${popularMovie.poster_path}`" alt="movie_poster" class="is-128x128">

        </figure>
      </div>
      <div class="card-content">
        <div class="media">
          <p class="title is-5">{{ popularMovie.title }}</p>
        </div>
        <p>{{popularMovie.release_date }}</p>
      </div>
    </div>
 


    <!-- <p>{{ popularMovie.title }}</p> -->
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    data() {
      return {
        moviePk: this.$route.params.movieId,
      }
    },
    computed: {
      ...mapGetters(['popularMovie']),
    },
    methods: {
      ...mapActions(['fetchPopularMoive'])
    },
    created() {
      this.fetchPopularMoive(this.moviePk)
    },
  }
</script>
<style>
</style>
