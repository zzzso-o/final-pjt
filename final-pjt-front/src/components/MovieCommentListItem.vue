<template>

  <div class="container">

    <hr class="opacity-50" id="hr">
    <div>
      <strong>{{ comment.user.username }}</strong>
      <span v-if="currentUser.username === comment.user.username && !isEditing">
        <button @click="switchIsEditing" class="button is-text is-small">Edit</button> 
        <button @click="deleteComment(payload)" class="button is-text is-small">Delete</button>
        {{ comment.movie_comment_created_at.substr(0,10)}} 
        {{ comment.movie_comment_created_at.substr(11,8)}} |
        {{ comment.movie_comment_updated_at.substr(0,10)}} 
        {{ comment.movie_comment_updated_at.substr(11,8)}} 
        
      </span>
    </div>
    <span v-if="!isEditing">
      {{ payload.movie_comment_content }}
      {{ payload.user_score }}

      
      </span>


    <span v-if="isEditing">
      <input type="text" v-model="payload.movie_comment_content">
      <input type="text" v-model="payload.user_score">
      <button @click="onUpdate" class="button is-text is-small">Update</button> 
      <button @click="switchIsEditing" class="button is-text is-small">Cancle</button>
    </span>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieCommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.comment.movie,
        commentPk: this.comment.pk,
        movie_comment_content: this.comment.movie_comment_content,
        movie_comment_created_at : this.comment.movie_comment_created_at,
        movie_comment_updated_at : this.comment.movie_comment_updated_at,
        user_score: this.comment.user_score
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['movieupdateComment', 'moviedeleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.movieupdateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
#hr{
  background-color: black;
  width: 90%;

  margin: 10px;

}
</style>
