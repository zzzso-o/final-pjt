<template>
  <div class="container">
    <h1 class="title">COMMUNITY</h1>
      <router-link 
        :to="{ name: 'articleNew' }">
        <button class="button is-right d-inline" ><i class="fa-solid fa-pencil fa-sm"></i> <strong>New</strong></button>
      </router-link>
      <b-colorpicker value="#CCC5DE" class="d-inline"/>
      <br>
      <table class="table table-hover">
        <tbody>
          <tr class="text-center">
            <th>No</th>
            <th>추천</th>
            <th>제목</th>
            <th>작성시간</th>
            <th>수정시간</th>
            <th>작성자</th>
          </tr>
          <tr class="text-center table-primary ">
            <th>전체공지</th>
            <th></th>
            <th>좋은말만 써주세요</th>
            <th></th>
            <th></th>
            <th>관리자</th>
          </tr>
          <tr v-for="article in articles" :key="article.pk" class="text-center">
            <th>{{ article.pk }}</th>
            <th>{{ article.like_count }}</th>
            <th>
              <router-link 
                :to="{ name: 'article', params: {articlePk: article.pk} }">
                {{ article.article_title }}({{ article.comment_count }})
              </router-link>
            </th>
            <th>{{ article.article_created_at }}</th>
            <th>{{ article.article_updated_at }}</th>
            <th>{{ article.user.username }}</th>
          </tr>
        </tbody>
      </table>





  </div>
  
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles']),
      ...mapGetters(['currentUser']),
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
    data() {
      return {
        
    }
  }
  }
</script>

<style>
.th{
  text-align: center;
}
.tr{
  text-align: center;
}
</style>

