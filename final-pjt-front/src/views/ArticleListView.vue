<template>
  <div class="container">
    <h1 class="title">COMMUNITY</h1>



      <router-link 
        :to="{ name: 'articleNew' }">
        <button class="button ">New </button>
      </router-link>
      <br>

      
<!--         
        {{ article.pk}} 
        {{ article.user.username }} : 
        
        <router-link 
          :to="{ name: 'article', params: {articlePk: article.pk} }">
          {{ article.article_title }}
        </router-link>
        

        ({{ article.comment_count }}) | +{{ article.like_count }} -->
      <table class="table table-hover">
       <thead> 
        <tr>
          <th >No</th>
          <th >작성자</th>
          <th >제목</th>
          <th >작성시간</th>
          <th >수정시간</th>
        </tr>
       </thead>
        <t-body >
        <!-- <b-table-column  field="id" label="ID" width="40"  numeric v-slot="article">
          {{ article.pk }}
        </b-table-column> -->
          <ul>
            <li v-for="article in articles" :key="article.pk">
              {{article.pk}}
              {{artucke.user}}
            </li>
            <!-- <td>{{article.pk}}</td>
            <td>{{article.user.username}}</td>
            <td>{{article.article_title}}</td>
            <td>{{article.article_title}}</td>
            <td>{{article.article_content}}</td> -->
            
          </ul>
        </t-body>
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
        data: [
          { 'no': 1, 'first_name': 'Jesse', 'last_name': 'Simmons', 'date': '2016-10-15 13:43:27', 'gender': 'Male' },
        ],
        columns: [
          {
            field: 'no',
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

