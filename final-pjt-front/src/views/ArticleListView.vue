<template>
  <div class="container">
    <h1 class="title">COMMUNITY</h1>
    <ul>
      <router-link 
        :to="{ name: 'articleNew' }">
        <button>글쓰기</button>
      </router-link>
      <li v-for="article in articles" :key="article.pk">
        {{ article.pk}}
        {{ article.user.username }} : 
        <router-link 
          :to="{ name: 'article', params: {articlePk: article.pk} }">
          {{ article.title }}
        </router-link>
        
        ({{ article.comment_count }}) | +{{ article.like_count }}

      </li>
    </ul>
  <!-- <b-table :data="data" :columns="columns"></b-table> -->

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
        data: [
          
        ],
        columns: [
          {
            field: 'id',
            label: 'No',
            width: '40',
            numeric: true
          },
          {
            field: 'first_name',
            label: 'Title',
          },
          {
            field: 'last_name',
            label: '작성자',
          },
          {
            field: 'date',
            label: 'Date',
            centered: true
          },
          {
            field: 'gender',
            label: 'Updated_Date',
          }
        ]
    }
  }
  }
</script>

<style></style>

