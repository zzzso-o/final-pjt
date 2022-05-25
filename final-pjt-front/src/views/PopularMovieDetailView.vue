<template>
  <div>
    
    <div class="container row">
      <h1 class="title">Movie Detail</h1>
    <div class=" col-4">
      <div>
        <img :src="`https://image.tmdb.org/t/p/w500${popularMovie.poster_path}`" alt="movie_poster" class="is-128x128">
      </div>
    </div>
    <div class="card col-8">
    <div class="card-content">
      <div class="content">
        <h1 class="title">{{ popularMovie.title }}({{ popularMovie.release_date.substr(0,4) }})</h1>
        <div class="facts">
          <span>
            {{popularMovie.release_date }}
          </span>
          <span class="genres">
            {{ popularMovie.genres[0].name}},
            {{ popularMovie.genres[1].name}},
            {{ popularMovie.genres[2].name}}
          </span>
          <span class="runtime">
              {{ popularMovie.runtime}}min
          </span>
        </div>
        <br>
        <div>
          <span class="fa fa-star checked fa-xl">{{ popularMovie.vote_average }}</span>
          <br>
          <!-- <div>
          <i class="fa-brands fa-gratipay fa-2x "></i>
          <i class="fa-brands fa-youtube fa-2x"></i>
          </div> -->
        </div>
        <br>
        <div>
          <span>{{ popularMovie.tagline }}</span>
        </div>
        <h2>overview</h2>
      </div>
      </div>
    </div>
    </div>
    {{ popularMovie.homepage }}
    {{ popularMovie.id }}
    {{ popularMovie.adult }}
    {{ popularMovie.genres }}
    {{ popularMovie.title }}
    {{ popularMovie.overview }}
    {{ popularMovie.release_date }}
    {{ popularMovie.vote_average }}
    {{ popularMovie.poster_path}}
    <div class="container">
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
.checked {
  color: orange;
}
.text-right{
  text-align: right;
}
</style>
