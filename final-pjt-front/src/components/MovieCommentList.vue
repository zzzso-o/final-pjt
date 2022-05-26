<template>
  <div class="container">
    
    <hr>
      <movie-comment-list-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk">
      </movie-comment-list-item>        


    
    <movie-comment-list-form></movie-comment-list-form>
  </div>
</template>

<script>
import MovieCommentListItem from '@/components/MovieCommentListItem.vue'
import MovieCommentListForm from '@/components/MovieCommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'MovieCommentList',
  components: { MovieCommentListForm, MovieCommentListItem },
  props: { comments: Array },
}
</script>

<style>

</style>
