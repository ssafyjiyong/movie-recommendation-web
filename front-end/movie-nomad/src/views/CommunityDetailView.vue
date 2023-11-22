<template>
  <div class="container" v-if="!loading">
    <div class="article-area">
      <h1>{{ currentArticle.title }}</h1>
      <div id='article-info'>
        {{ currentArticle.user['nickname'] }} | {{ currentArticle.movie }} | 마지막 수정일 : {{
          currentArticle.updated_at.substr(0, 10) }}
      </div>
      <hr>
      <p>{{ currentArticle.content }}</p>
    </div>
    <div class="comment-area">
      <h1>comment</h1>
    </div>
  </div>

  <div v-else class="d-flex justify-content-center align-items-center m-5">
    <div class="spinner-border text-success d-inline" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
    <h3 class="m-3">{{ randomMessage }}</h3>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router'
import { getArticleDetail, getMovieDetail } from '@/apis/movieApi'
import { useMovieStore } from '@/stores/movieStore';

const movieStore = useMovieStore()
const randomMessage = movieStore.loadingMessage[Math.floor(Math.random() * movieStore.loadingMessage.length)];

const currentArticle = ref([])
const movie = ref('')
const route = useRoute()
const articlePk = route.params.articleId

const loading = ref(true)

const initializeArticleDetail = (articlePk) => {
  getArticleDetail(articlePk)
    .then((response) => {
      currentArticle.value = response.data
    })
    .catch((error) => {
      console.error('Error initializing article detail:', error)
    })
  loading.value = false
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