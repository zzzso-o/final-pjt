<template>
<b-notification aria-close-label="Close notification" type="is-danger is-light">
  <div class="comment-error-list">
    
    <p v-for="(errors, field) in commentError" :key="field">
      {{ field }}
      <ul>
        <li v-for="(error, idx) in errors" :key="idx">
          {{ error }}
        </li>
      </ul>
    </p>

  </div>
</b-notification>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'CommentErrorList',
    computed: {
      ...mapGetters(['commentError'])
    },
  }
</script>

<style>
  .comment-error-list {
    color: palevioletred;
  }
</style>
