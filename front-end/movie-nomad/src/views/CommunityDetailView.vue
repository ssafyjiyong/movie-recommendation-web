<template>
  <div class="container mb-5 mt-3 text-black">

    <div class="article-area">

      <!-- 글 제목 -->
      <div class="py-3 px-4 d-flex justify-content-between align-items-end">
        <div class="flex-grow-1">
          <h3>{{ currentArticle.title }}</h3>
        </div>

        <div v-if="loadingMovieInfo" class="text-end aboutMovie">
          <span>영화 </span>
          <span @click="goToDetail" class="cursorEffect fs-5">'{{ movieTitle }}'</span>
          <span>에 대하여</span>
        </div>
        <div v-else class="text-end aboutMovie">
          <span>관련 영화 정보를 찾고 있습니다 </span>
          <div class="spinner-border text-success spinner-border-sm" role="status">
            <span class="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>

      <div class="d-flex justify-content-between px-3 py-2 bg-white">
        <div class='article-info' v-if="currentArticle.user">
          <span>{{ currentArticle.user['nickname'] }} |
            마지막 수정일 : {{ currentArticle.updated_at.substr(0, 10) }}</span>
        </div>

        <div>
          <i class="fa-solid fa-heart text-danger mx-1"></i>
          <span>{{ currentArticle.like_user_count }}</span>
        </div>
      </div>

      <div class="p-3">
        <div v-if="imageExist" class="text-center">
          <img 
          :src="`http://localhost:8000${currentArticle.image}`" 
          alt="image">
        </div>
        <p class="fs-5">{{ currentArticle.content }}</p>
      </div>

      <div class="d-flex justify-content-center">
        <button 
        @click="likeArticle"
        class="btn btn-custom">
        <i class="fa-regular fa-thumbs-up"></i> 
        좋아요 | {{ currentArticle.like_user_count }}
        </button>
      </div>
    </div>

    <div class="d-flex justify-content-end m-3">
      <small class="cursorEffect" @click="updateArticle">수정</small>
      <small class="mx-1">|</small>
      <small class="cursorEffect" @click="deleteTheArticle">삭제</small>
    </div>

    <!-- 여기서부터 댓글입니다 -->

    <div class="comment-area">

      <div class="bg-white px-3 py-2">
        <p class="m-0">댓글</p>
      </div>

      <!-- 댓글 작성란 -->
      <div>
        <form>
          <div class="mb-3">
            <label for="formControlInput" class="form-label"></label>
            <input type="text" class="form-control w-75 d-inline-block m-2" id="formControlInput" placeholder="욕설/비난 시 회원 탈퇴입니다.">
            <button type="submit" class="btn btn-success">댓글 작성</button>
          </div>
        </form>
      </div>

      <CommentCard />

    </div>
    <div>
      <button 
      @click="goBack"
      class="btn btn-back-custom mx-2 mb-2">뒤로가기</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router'
import { getArticleDetail, deleteArticleAPI, getMovieDetail } from '@/apis/movieApi'
import CommentCard from '@/components/community/CommentCard.vue';
import { computed } from '@vue/reactivity';
import { likeArticleApi } from '@/apis/movieApi';

const currentArticle = ref([])
const route = useRoute()
const router = useRouter()
const articlePk = route.params.articleId
const movieTitle = ref('')
const moviePk = ref(0)
const articleImage = ref(false)
const alreadyLike = ref(false)

const loadingMovieInfo = ref(false)

const imageExist = computed(() => {
  return articleImage.value
})

// 영화 디테일로 이동
const goToDetail = function () {
  router.push(`/moviedetail/${moviePk.value}`)
}

const goBack = function () {
  router.push(`/community/${route.params.category}`)
}

const likeArticle = function () {
  likeArticleApi(route.params.articleId)
  .then(() => {
    if (alreadyLike.value === false) {
      currentArticle.value.like_user_count += 1;
      alreadyLike.value = true
    } else {
      currentArticle.value.like_user_count -= 1;
      alreadyLike.value = false
    }
    })
    .catch((error) => {
      console.error('Error liking article:', error)
    })
}

const initializeArticleDetail = (articlePk) => {
  getArticleDetail(articlePk)
    .then((response) => {
      console.log(response.data)
      currentArticle.value = response.data
      if (response.data.image !== null) {
        articleImage.value = true
      }
    })
    .then(() => {
      getMovieDetail(currentArticle.value.movie)
        .then((response) => {
          movieTitle.value = response.data['title']
          moviePk.value = response.data['pk']
          loadingMovieInfo.value = true
        })
    })
    .catch((error) => {
      console.error('Error initializing article detail:', error)
    })
}

const deleteTheArticle = function () {
  deleteArticleAPI(articlePk)
    .then((response) => {
      router.replace(`/community/${currentArticle.value.category}`)
    })
}

const updateArticle = function () {
    router.replace(`/community/update/${route.params.articleId}/${currentArticle.value.category}`)
}

onMounted(() => {
  initializeArticleDetail(articlePk)
});

</script>

<style scoped>
.aboutMovie { 
  min-width: 230px;
}
.btn-custom {
  background-color: #FBDFDF;
  color: #EC5E5E;
}

.btn-custom:hover {
  background-color: #EC5E5E;
  color: white;
}

.btn-back-custom:hover {
  background-color: #b3b6b8;
  color: black
}

.btn-back-custom {
  background-color: gray;
  color: white;
}

.container {
  width: 80%;
  border-radius: 20px;
  padding: 1%;
  background-color: #f6ffe8;
}
img {
  max-width: 90%;
}

.cursorEffect {
  cursor: pointer;
}

.article-info {
  text-align: right;
}</style>