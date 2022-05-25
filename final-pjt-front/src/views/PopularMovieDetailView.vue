<template>
  <div>
    
    <div class="container row" id="detail_container" v-if=!!popularMovie.title> 
      <h1 class="title">Movie Detail</h1>
    <div class=" col-4">
      <div>
        <img :src="`https://image.tmdb.org/t/p/w500${popularMovie.poster_path}`" alt="movie_poster" class="is-128x128">
      </div>
    </div>
    <div class="card col-8">
    <div class="card-content">
      <div class="content" >
        <h1 class="title" id="movietitle">{{ popularMovie.title }}({{ popularMovie.release_date.substr(0,4) }})</h1>
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
    <div class="container" v-else>
      tmdb에서 정보를 볼러올 수 없습니다 
      영화 정보가 존재하지 않아요 
      뒤로가기 버튼으로 다른 영화를 조회해주세요 
    </div>
    <!-- {{ popularMovie.homepage }}
    {{ popularMovie.id }}
    {{ popularMovie.adult }}
    {{ popularMovie.genres }}
    {{ popularMovie.title }}
    {{ popularMovie.overview }}
    {{ popularMovie.release_date }}
    {{ popularMovie.vote_average }}
    {{ popularMovie.poster_path}} -->
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
/* .facts{
  margin-top: 0px;
} */
#movietitle{
  margin-bottom: 0;
}
#detail_container{
  width: 850px;
}
</style>
