<template>
  <div class="container">
    
      <comment-list-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk">
      </comment-list-item>        


    <comment-list-form></comment-list-form>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentListForm from '@/components/CommentListForm.vue'

import { mapGetters } from 'vuex'

// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentListForm, CommentListItem,  },
  props: { comments: Array },
  computed:{
    ...mapGetters(['commentError'])
  }
}
</script>

<style>

</style>
