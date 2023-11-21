<template>
  <div class="container">
    <div class="article-area">
      <h1>{{ currentArticle.title }}</h1>
      <div id='article-info'>
        {{ currentArticle.user['nickname'] }} | {{ currentArticle.movie }} | 마지막 수정일 : {{ currentArticle.updated_at.substr(0, 10) }}
      </div>
      <hr>
      <p>{{ currentArticle.content }}</p>
    </div>
    <div class="comment-area">
      <h1>comment</h1>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router'
import { getArticleDetail } from '@/apis/movieApi'

const props = defineProps({
  article: Object
})

const currentArticle = ref('')
const route = useRoute()
const articlePk = route.params.articleId


const initializeArticleDetail = (articlePk) => {
  getArticleDetail(articlePk)
  .then((response) => {
    if (response && response.data) {
        currentArticle.value = response.data
      }
    })
    .catch((error) => {
      console.error('Error initializing article detail:', error)
    })
}

onMounted(() => {
  initializeArticleDetail(articlePk)
});

</script>

<style scoped>
.container {
  max-width: 90%;
}

.article-area {
  border: 1px black solid;
  border-radius: 10px;
  margin-top: 30px;
  padding: 20px;
}

.comment-area {
  border: 1px solid black;
  border-radius: 10px;
  margin-top: 30px
}

#article-info {
  text-align: right;
}
</style>