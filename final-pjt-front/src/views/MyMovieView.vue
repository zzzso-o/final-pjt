<template>
  <div class="container">
    <!-- <movie-recommend></movie-recommend> -->
    <h2>{{ currentUser.username }}님을 위한 추천영화 !</h2>

    <div>
    <h1>{{ profile.username }}</h1>

    <h2>작성한 글</h2>
    <ul>
      <li v-for="article in profile.articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.article_title }}
        </router-link>
      </li>
    </ul>

    <h2>좋아요 한 글</h2>
    <ul>
      <li v-for="article in profile.article_likes" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.article_title }}
        </router-link>
      </li>
    </ul>
    <h2>평점을 남긴영화</h2>
    <ul>
      {{ profile}}

    </ul>

  </div>
        <!-- {{ popularMovies}} -->
    <div v-for="movie in popularMovies" :key="movie.pk" >
      <!-- {{ movie }} -->
        <div v-for="comment in profile.comment_user" :key="comment.pk">
        <!-- {{ comment.movie }} -->
        <div v-if="movie.pk === comment.movie">
          recommend = {{ movie.genres[0]}}
        </div>
      </div>
    </div>
    getrecommend()
  </div>

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
// import MovieRecommend from '../components/MovieRecommend.vue'

export default {
  data() {
    return {
      recommend: [],

    }
  },
  components:{
    
  },
  computed:{
    ...mapGetters(['currentUser']),
    ...mapGetters(['profile']),
    ...mapGetters(['popularMovies']),
    getrecommend(){
      for(const moviepk of this.PopularMovies){
        for(const comment_user of this.profile.comment_user){
          if(moviepk === comment_user.movie){
            return moviepk.genres[0]
            }
          else{
            return false
          }
        }
      }
      return false
    }

  },
  methods: {
    ...mapActions(['fetchProfile']),
    ...mapActions(['fetchPopularMovies']),
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
    this.fetchPopularMovies()
  },


}
// user가 평점을 남긴 영화의 장르를 가져와서 
// 
</script>

<style>

</style>
