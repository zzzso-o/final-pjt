<template>

  <div class="container" >

    <hr class="opacity-50" id="hr">
    
      <!-- 기본적으로 위쪽에 들어가는 곳 -->
      <div id="comment-title">
      <strong>{{ comment.pk }}. {{ comment.user.username }}</strong>
      <span v-if="currentUser.username === comment.user.username && !isEditing">
        <button @click="switchIsEditing" class="button is-text is-small">Edit</button> 
        <button @click="moviedeleteComment(payload)" class="button is-text is-small">Delete</button>
        <button class="button is-text is-small disabled">
        {{ (comment.movie_comment_created_at+'').substr(0,10)}} 
        {{ (comment.movie_comment_created_at+'').substr(11,8)}} |
        {{ (comment.movie_comment_updated_at+'').substr(0,10)}} 
        {{ (comment.movie_comment_updated_at+'').substr(11,8)}}
        </button> 
      </span>
      </div>
    <!-- Edit하는 중이 아닐 때 보여주는 곳 -->
    <span v-if="!isEditing"> 
      <div class="container" >
        <div class="heart-ratings ml-3">
          <div 
            class="heart-ratings-fill space-x-2 text-lg"
            :style="{ width: ratingToPercent + '%' }"
          >
          <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
          </div>
          <div class="heart-ratings-base space-x-2 text-lg">
            <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
          </div>
        </div>
        <div class="container commentbox">
        {{ payload.movie_comment_content }}
        </div>
      </div>
    </span>
        
          <!-- Edit하고 있을 때 -->
          <span v-if="isEditing">
            <div class="buttons has-addons d-inline">
              <button @click="onUpdate" class="button is-text is-small">Update</button> 
              <button @click="switchIsEditing" class="button is-text is-small">Cancle</button>
            </div>
           <button class="button is-text is-small disabled">
            {{ (comment.movie_comment_created_at+'').substr(0,10)}} 
            {{ (comment.movie_comment_created_at+'').substr(11,8)}} |
            {{ (comment.movie_comment_updated_at+'').substr(0,10)}} 
            {{ (comment.movie_comment_updated_at+'').substr(11,8)}}
            </button>
            <!-- <input type="text" v-model="payload.user_score"> -->
            <div class="container">
            <!-- <div class="rate">
              <b-field>
                  <b-radio v-model="payload.user_score"
                      native-value="1">
                      <i>★</i>
                  </b-radio>
              </b-field>
              <b-field>
                <b-radio v-model="payload.user_score"
                    native-value="2"
                    >
                    <i>★★</i>
                </b-radio>
              </b-field>
              <b-field>
                <b-radio v-model="payload.user_score"
                    native-value="3"
                    >
                    <i>★★★</i>
                </b-radio>
              </b-field>
              <b-field>
                <b-radio v-model="payload.user_score"
                    native-value="4">
                  <i>★★★★</i>
                </b-radio>
              </b-field>
              <b-field>
                <b-radio v-model="payload.user_score"
                    native-value="5">
                    <i>★★★★★</i>
                </b-radio>
              </b-field>
            </div> -->
            <b-input type="textarea" size="is-small"  maxlength="100" v-model="payload.movie_comment_content"></b-input> 
          </div>
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
  width: 100%;
  margin: 10px;

}
.heart-ratings {
  font-size: 1rem;
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
.button{
  width : 20;
}
div#comment-title{
  margin-top: 20px;
  padding-left: 25px;
}
.commentbox{
  margin-left: 2px;
  margin-top: 6px;
  font-size: xx-small;

}

</style>
