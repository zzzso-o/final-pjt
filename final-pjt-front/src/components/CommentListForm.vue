<template>
<div class="comment-container">
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <b-input type="textarea" id="comment" v-model="article_comment_content" required></b-input>
    <button class="button is-text is-small" >Comment</button>
  </form>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      article_comment_content: ''
    }
  },
  computed: {
    ...mapGetters(['article']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ 
        articlePk: this.article.pk, 
        article_comment_content: this.article_comment_content, })
      this.article_comment_content = ''
    }
  }
}
</script>

<style>
.comment-list-form {
  border: 0px solid black;
  margin: 1rem;
  padding: 1rem;
}
.comment-container{
  margin-left:0px;
  padding-left:0px;
}
</style>
