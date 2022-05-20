<template>
  <div>
    <h1>Home</h1>
    <ul>
      <li v-for="article in articles" :key="article.pk">
        
        {{ article.pk}}
        {{ article.user.username }} : 

        <router-link 
          :to="{ name: 'article', params: {articlePk: article.pk} }">
          {{ article.title }}
        </router-link>
        =>
        ({{ article.comment_count }}) | +{{ article.like_count }}

      </li>
    </ul>
  <b-table :data="data" :columns="columns"></b-table>

  </div>
  
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles'])
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
          { 'id': 1, 'first_name': 'Jesse', 'last_name': 'Simmons', 'date': '2016-10-15 13:43:27', 'gender': '2016-12-06 14:38:38' },
          { 'id': 2, 'first_name': 'John', 'last_name': 'Jacobs', 'date': '2016-12-15 06:00:53', 'gender': '2016-12-06 14:38:38' },
          { 'id': 3, 'first_name': 'Tina', 'last_name': 'Gilbert', 'date': '2016-04-26 06:26:28', 'gender': '2016-12-06 14:38:38' },
          { 'id': 4, 'first_name': 'Clarence', 'last_name': 'Flores', 'date': '2016-04-10 10:28:46', 'gender': '2016-12-06 14:38:38' },
          { 'id': 5, 'first_name': 'Anne', 'last_name': 'Lee', 'date': '2016-12-06 14:38:38', 'gender': '2016-12-06 14:38:38' }
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

