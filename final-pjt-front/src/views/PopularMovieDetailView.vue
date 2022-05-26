<template>
  <div>
    <div class="container row" id="detail_container" > 
      <h1 class="title">Movie Detail</h1>
    <div class=" col-4">
      <div>
        <img :src="`https://image.tmdb.org/t/p/w500${popularMovie.poster_path}`" alt="movie_poster" class="is-128x128">
      </div>
    </div>
    <div class="card col-8">
    <div class="card-content">
      <div class="content" >
        <h1 class="title" id="movietitle">{{ popularMovie.title }}({{ (popularMovie.release_date+'').substr(0,4) }})</h1>
        <div class="facts">
          <span>
            {{popularMovie.release_date }}
          </span>
          <span class="genres">
            <!-- {{ popularMovie.genres}}, -->
          </span>
          <!-- <span class="runtime">
              {{ popularMovie.runtime}}min
          </span> -->
        <!-- </div>
        <em>{{ popularMovie.tagline }}</em>
        <div> -->
          <span class="fa fa-star checked fa-xl">{{ popularMovie.vote_average }}</span>
        </div>
        <h2 id="overview-title">overview</h2>
        {{ popularMovie.overview }}
      </div>
      </div>
    </div>
    </div>


    <movie-comment-list :comments="popularMovie.comments">dd</movie-comment-list>

  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import MovieCommentList from '@/components/MovieCommentList.vue'

  export default {
    components: { MovieCommentList },
    data() {
      return {
        movieId: this.$route.params.movieId,
      }
    },
    computed: {
      ...mapGetters(['popularMovie']),
    },
    methods: {
      ...mapActions(['fetchPopularMovie'])
    },
    created() {
      this.fetchPopularMovie(this.movieId)
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
/* .facts{
  margin-top: 0px;
} */
#movietitle{
  margin-bottom: 0;
}
#detail_container{
  width: 850px;
}
#overview-title{
  margin :0
}
</style>
