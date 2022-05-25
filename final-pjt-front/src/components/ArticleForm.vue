<template>
  <div >
    <!-- <h1 class="title">새 글 작성</h1>
    <div class="box">
      <form @submit.prevent="onSubmit">
        <div>
          <input v-model="newArticle.title" id="title" 
          class="input is-link " placeholder="제목을 입력하세요"/>
        </div>
        <br>
        <div>
          <textarea v-model="newArticle.content" type="text" id="content" class="textarea is-link is-hovered is-large"
          placeholder="영화에 관한 토론은 언제나 환영입니다!╰(*°▽°*)╯"></textarea>
        </div>
        <br>
        <div>
          <button>{{ action }}</button>
        </div>
      </form>
    </div> -->
  <form @submit.prevent="onSubmit">
    <div>
      <label for="title">title: </label>
      <input v-model="newArticle.article_title" type="text" id="article_title" />
    </div>
    <div>
      <label for="content">contnet: </label>
      <textarea v-model="newArticle.article_content" type="text" id="article_content"></textarea>
    </div>
    <div>
      <button>{{ action }}</button>
    </div>
  </form>


  </div>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          article_title: this.article.article_title,
          article_content: this.article.article_content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }

</script>

<style></style>
