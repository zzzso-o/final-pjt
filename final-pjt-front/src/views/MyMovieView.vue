<template>
  <div class="container">
    {{ profile}}
    <!-- <movie-recommend></movie-recommend> -->
    <h2 class="title">🧍‍♂️  {{ currentUser.username }}님을 위한 추천영화 !</h2>
    
    <div v-for="movie in popularMovies" :key="movie.pk" >
      <div v-for="comment in profile.comment_user.slice(0,1)" :key="comment.pk">
        <div v-if="movie.pk === comment.movie"> 
          <!-- 프로필 유저가 좋아한 pk랑 무비안에 pk랑 맞으면? = 
          1. 장르를 가져와서 
          2. 또 무비를 한번돌면서 
          3. 장르 id가 같은 영화를 가져옴
          {{ movie.genres[0]}} -->
          <div v-for="mov in popularMovies.slice(0,20)" :key="mov.pk" >
            <div v-if="movie.genres[0] === mov.genres[0]">
              <div class="container box">
                <router-link :to="{ name: 'movie', params: {movieId: mov.pk} }">
                <strong>{{ mov.title}}</strong>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div>
    <hr>
    <h2 class="title">{{profile.username }} 님이 작성한 글 리스트 </h2>
    <div class="container box">
      <ul>
        <li v-for="article in profile.articles" :key="article.pk">
          <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
            {{ article.article_title }}
          </router-link>
        </li>
      </ul>
    </div>

    <h2 class="title">{{profile.username }} 님이 좋아한 글 리스트 </h2>
    <div class="container box">
    <ul>
      <li v-for="article in profile.article_likes" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.article_title }}
        </router-link>
      </li>
    </ul>
    </div>
    <h2 class="title">{{ profile.username }} 님이 평점을 남긴 영화 </h2>
    
    <div class="container box">
      comment 확인하러 가기 ! 
    <ul>
      <div v-for="comment in profile.comment_user" :key="comment.pk">
        <router-link :to="{ name: 'movie', params: {movieId: comment.movie} }">
        <strong>{{ comment.movie}}</strong>
        </router-link>
      </div>
    </ul>
    </div>
  </div>


  </div>

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'
// import MovieRecommend from '../components/MovieRecommend.vue'

export default {
  data() {
    return {
      recommend: [],
      startnumbers: _.range(1,10),
      endnumbers: _.range(30,40),
      endrannum: _.sampleSize(this.endnumbers,2)
    }
  },
  components:{
    
  },
  computed:{
    ...mapGetters(['currentUser']),
    ...mapGetters(['profile']),
    ...mapGetters(['popularMovies']),


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
