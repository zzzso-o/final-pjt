<template>

  <div class="container">

    <hr class="opacity-50" id="hr">
    <div>
      <strong>{{ comment.user.username }}</strong>
      <span v-if="currentUser.username === comment.user.username && !isEditing">
        <button @click="switchIsEditing" class="button is-text is-small">Edit</button> 
        <button @click="moviedeleteComment(payload)" class="button is-text is-small">Delete</button>
        {{ (comment.movie_comment_created_at+'').substr(0,10)}} 
        {{ (comment.movie_comment_created_at+'').substr(11,8)}} |
        {{ (comment.movie_comment_updated_at+'').substr(0,10)}} 
        {{ (comment.movie_comment_updated_at+'').substr(11,8)}} 
        
      </span>
    </div>
    <span v-if="!isEditing">
      <div class="container" >
        <div class="heart-ratings ml-3">
          <div 
            class="heart-ratings-fill space-x-2 text-lg"
            :style="{ width: ratingToPercent + '%' }"
          >
          <span>★</span><span>★</span><span>★</span><span>★</span>
          </div>
          <div class="heart-ratings-base space-x-2 text-lg">
            <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
          </div>
        </div>
        {{ payload.movie_comment_content }}
      </div>
    </span>
        <div class="container">
          <span v-if="isEditing">
            <input type="text" v-model="payload.movie_comment_content">
            <input type="text" v-model="payload.user_score">
            <button @click="onUpdate" class="button is-text is-small">Update</button> 
            <button @click="switchIsEditing" class="button is-text is-small">Cancle</button>
          </span>
        </div>
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
    ratingToPercent() {
      const score = +this.comment.user_score * 20;
      return score + 1.5;
    },
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
.heart-ratings {
  font-size: 1.5rem;
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: #959595;
}
 
.heart-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: orange;
}
 
.heart-ratings-base {
  z-index: 0;
  padding: 0;
}
</style>
