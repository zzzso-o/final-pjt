<template>

  <div class="container">
    <hr class="opacity-50" id="hr">
    <div>
      <strong>{{ comment.user.username }}</strong>
      <span v-if="currentUser.username === comment.user.username && !isEditing">
        <button @click="switchIsEditing" class="button is-text is-small">Edit</button> 
        <button @click="deleteComment(payload)" class="button is-text is-small">Delete</button>
        <button class="button is-text is-small" disabled>
        {{ (comment.article_comment_created_at+'').substr(0,10)}} 
        {{ (comment.article_comment_created_at+'').substr(11,8)}} |
        {{ (comment.article_comment_updated_at+'').substr(0,10)}} 
        {{ (comment.article_comment_updated_at+'').substr(11,8)}}
        </button> 
        
      </span>
    </div>
    <span v-if="!isEditing">{{ payload.article_comment_content }}</span>
    <span v-if="isEditing">
        <div class="buttons has-addons d-inline">
          <button @click="onUpdate" class="button is-text is-small">Update</button> 
          <button @click="switchIsEditing" class="button is-text is-small">Cancle</button>
        </div>
        <button class="button is-text is-small" disabled >
        {{ (comment.article_comment_created_at+'').substr(0,10)}} 
        {{ (comment.article_comment_created_at+'').substr(11,8)}} |
        {{ (comment.article_comment_updated_at+'').substr(0,10)}} 
        {{ (comment.article_comment_updated_at+'').substr(11,8)}}
        </button>
      <b-input type="textarea" size="is-small"  maxlength="100" v-model="payload.article_comment_content"></b-input>
    </span>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        article_comment_content: this.comment.article_comment_content,
        article_comment_created_at : this.comment.article_comment_created_at,
        article_comment_updated_at : this.comment.article_comment_updated_at,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>

</style>
