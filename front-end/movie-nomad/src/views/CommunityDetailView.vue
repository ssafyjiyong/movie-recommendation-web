<template>
  <div class="container" v-if="!loading">

    <div class="article-area">
      <h1>{{ currentArticle.title }}</h1>
      <div class='article-info' v-if="currentArticle.user">
        {{ currentArticle.user['nickname'] }} |
        마지막 수정일 : {{ currentArticle.updated_at.substr(0, 10) }}
      </div>
      <div class="article-info">
        <RouterLink :to="{ name: 'moviedetail', params: { movieId: moviePk } }">{{ movieTitle }}</RouterLink>
      </div>
      <hr>
      <p>{{ currentArticle.content }}</p>

      <div class="d-flex justify-content-center">
        <button>이 게시글 좋아요</button>
      </div>
    </div>

    <div class="d-flex justify-content-end">
      <button>게시글 수정</button>
      <button @click="deleteTheArticle">게시글 삭제</button>
    </div>

    <!-- 여기서부터 댓글입니다 -->

    <div class="comment-area">

      <div>
        <p>xx개의 댓글이 있습니다</p>
      </div>

      <!-- 댓글 작성란 -->
      <div>
        <form>
          <input type="text">
          <input type="submit">
        </form>
      </div>
      <hr>
      <CommentCard />

    </div>
  </div>

  <!-- 로딩중에 나오는 명대사 -->
  <div v-else class="d-flex justify-content-center align-items-center m-5">
    <div class="spinner-border text-success d-inline" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
    <h3 class="m-3">{{ randomMessage }}</h3>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router'
import { getArticleDetail, deleteArticleAPI, getMovieDetail } from '@/apis/movieApi'
import { useMovieStore } from '@/stores/movieStore';
import CommentCard from '@/components/community/CommentCard.vue';

defineProps({
  isDarkMode: Boolean,
})

const movieStore = useMovieStore()
const randomMessage = movieStore.loadingMessage[Math.floor(Math.random() * movieStore.loadingMessage.length)];

const currentArticle = ref([])
const route = useRoute()
const router = useRouter()
const articlePk = route.params.articleId
const movieTitle = ref('')
const moviePk = ref(0)

const loading = ref(true)

const initializeArticleDetail = (articlePk) => {
  getArticleDetail(articlePk)
    .then((response) => {
      currentArticle.value = response.data
    })
    .then(() => {
      getMovieDetail(currentArticle.value.movie)
        .then((response) => {
          // console.log(response)
          movieTitle.value = response.data['title']
          moviePk.value = response.data['pk']
        })
    })
    .catch((error) => {
      console.error('Error initializing article detail:', error)
    })
  loading.value = false
}

const deleteTheArticle = function () {
  deleteArticleAPI(articlePk)
    .then((response) => {
      router.replace(`/${currentArticle.value.category}`)
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

.article-info {
  text-align: right;
}
</style>