<template>
<div>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <label for="comment">comment: </label>
    <input type="text" id="comment" v-model="movie_comment_content" required>
    <label for="comment">user_score: </label>
    <input type="text" id="user_score" v-model="user_score" required>
    <button>Comment</button>
  </form>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieCommentListForm',
  data() {
    return {
      movie_comment_content: '',
      user_score: ''

    }
  },
  computed: {
    ...mapGetters(['popularMovie', 'currentUser']),
  },
  methods: {
    ...mapActions(['moviecreateComment', 'fetchCurrentUser']),
    onSubmit() {
      // if (this.CurrentUser){
      //   pass
      // }
      // else{
        this.moviecreateComment({ 
        moviePk: this.popularMovie.pk, 
        movie_comment_content: this.movie_comment_content,
        user_score: this.user_score, })
        this.movie_comment_content = ''
      }

    // }
  },
  created(){
    // fetchCurrentUser()
  }
}
</script>

<style>
.comment-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>
