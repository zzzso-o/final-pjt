<template>
<div>
  <div class="container box">
    <div class="content">
    <div class="titlecontainer">
      <strong>{{ article.article_title }}</strong>
        <span>
          <button disabled class= "button is-text is-small d-inline">
          <strong>{{ article.user.username }}</strong> | 
          {{ (article.article_created_at+'').substr(0,10) }} | {{ article.article_created_at.substr(11,8) }}
          </button>
        </span>
        <span class="article-user">
          <button
        class= "button is-text is-small"
        @click="likeArticle(articlePk)"
      ><strong>추천 {{ likeCount }}</strong></button>
        </span>
    </div>
    <div class="contents-container">
      <p>
        {{ article.article_content }}
      </p>
    </div>
    
    <div class="footer-container">
      <div v-if="isAuthor">
        <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <button class="button is-text is-small">Article Edit</button>
        </router-link>
        <button @click="deleteArticle(articlePk)" class="button is-text is-small">Article Delete</button>
      </div>
    </div>
    <div>
    

    </div>
    
    </div>

    

  </div>
    <comment-list :comments="article.comments">dd</comment-list>
</div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'

  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.article_likes?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>
<style>
.titlecontainer{
  width: 430px;
  margin: 30px;
}
.contents-container{
  margin: 30px;
  height: 500px;

}
.article-info{
  text-align: justify;
}
/* .footer-container{
  margin:30px;
} */
</style>
