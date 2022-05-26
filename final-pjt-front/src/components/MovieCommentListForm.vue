<template>
<div>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <!-- <input type="text" required> -->
 
    <div class="rate">
      <b-field>
          <b-radio v-model="user_score"
              native-value="1">
              <i>★</i>
          </b-radio>
      </b-field>
      <b-field>
        <b-radio v-model="user_score"
            native-value="2"
            >
            <i>★★</i>
        </b-radio>
      </b-field>
      <b-field>
        <b-radio v-model="user_score"
            native-value="3"
            >
            <i>★★★</i>
        </b-radio>
      </b-field>
      <b-field>
        <b-radio v-model="user_score"
            native-value="4">
          <i>★★★★</i>
        </b-radio>
      </b-field>
      <b-field>
        <b-radio v-model="user_score"
            native-value="5">
            <i>★★★★★</i>
        </b-radio>
      </b-field>
      
    </div>
    <b-field label="Message">
      <input maxlength="100" type="textarea" id="comment" v-model="movie_comment_content" >
    </b-field>
    <button class="button">등록</button>
    
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
      this.moviecreateComment({ 
      moviePk: this.popularMovie.pk, 
      movie_comment_content: this.movie_comment_content,
      user_score: this.user_score, })

      this.movie_comment_content = ''
    },

    myFunction(){
      alert('click')
      console.log('click')
    }

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
.rate i, .rate i:hover ~ i {
  color: #222;
  text-shadow: none;
  transition: color 200ms,
              text-shadow 200ms;
  /* This will remove the delay when
     moving the cursor left or right
     within the set of stars. */
  transition-delay: 0;
}

/* This is the style that will be
   applied to all stars and then
   subsequently removed from the stars
   to the right of the one being
   hovered. */
.rate:hover i {
  color: #fc0;
  text-shadow: #fc0 0 0 20px;
}

/* Make the effect apply one star at a
   time. Limiting the selector to when
   .rate is hovered removes the effect
   without delay when cursor leaves
   the .rate area. */
.rate:hover i:nth-child(2) {
  transition-delay: 30ms;
}

.rate:hover i:nth-child(3) {
  transition-delay: 60ms;
}

.rate:hover i:nth-child(4) {
  transition-delay: 90ms;
}

.rate:hover i:nth-child(5) {
  transition-delay: 120ms;
}

/* Miscellaneous styles. */
.rate i {
  cursor: pointer;
  font-style: normal;
}

</style>
