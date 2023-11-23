<template>
  <div class="topTopBox">
    <div class="theTopBox">
      <div class="d-flex justify-content-between">
      <div class="m-3">
        <i class="fa-solid fa-comment-dots fa-lg mx-2"></i><span class="fw-bold textColor">영화토크</span>
      </div>
      <div>
          <button class="btn btn-custom btn-sm fw-bold mt-3 me-3" @click="goToAddArticle">글쓰기</button>
        </div>
      </div>

      <div class="topArticleBox">
        <div class="latest-article">
          <div class="articleBox d-flex text-center justify-content-between">
            <div class="col-1 py-3">글번호</div>
            <div class="col-7 py-3">글제목</div>
            <div class="col-2 py-3">작성자</div>
            <div class="col-2 py-3">작성일</div>
          </div>
          <hr class="m-0">
          <div v-for="(searchedArticle, idx) in paginatedArticles" :key="idx">
            <div id="articleList" class="d-flex text-center justify-content-between">
              <div class="col-1 py-2">{{ searchedArticle.id }}</div>
              <div @click="goToDetail(searchedArticle.id)" class="articleTitle col-7 py-2">{{ searchedArticle.title }}</div>
              <div class="col-2 py-2">{{ searchedArticle.user.nickname }}</div>
              <div class="col-2 py-2">{{ formatDate(searchedArticle.created_at) }}</div>
            </div>
            <hr class="m-0">
          </div>
        </div>
        <!-- 더 보기 버튼 -->
        <div class="d-flex justify-content-center m-3">
          <button class="btn btn-custom fw-bold" @click="loadMoreArticles">댓글 더 보기</button>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { getArticlesList } from '@/apis/movieApi';

defineProps({
  isDarkMode: Boolean,
})

const router = useRouter()
const allArticles = ref([])


// 페이지 상태 관리
const itemsPerPage = 20
const page = ref(1)

// 페이지에 따라 데이터 범위 조정(최초 첫 번째 페이지 데이터 로드)
const paginatedArticles = computed(() => {
  return allArticles.value.slice(0, end.value)
})

const start = ref(0)
const end = ref(14)
// 더 보기 버튼 클릭 시 페이지 상태 증가
const loadMoreArticles = () => {
  start.value = page.value * itemsPerPage
  end.value = start.value + itemsPerPage
  page.value++
}


const goToAddArticle = function () {
  router.push('/create/1/')
}

const formatDate = (dateStr) => {
  const date = new Date(dateStr);
  return date.toLocaleDateString('ko-KR', { year: '2-digit', month: '2-digit', day: '2-digit' });
}

const goToDetail = function (articleId) {
  router.push(`/communitydetail/${articleId}`)
}

onMounted(() => {
  getArticlesList()
    .then(response => {
      allArticles.value = response.data.filter((article) => {
        return article.category === 'talk'
      })
    })
});
</script>

<style scoped>
#articleList:hover {
  background-color: rgb(248, 248, 248);
  font-weight: bold;
  color: rgb(99, 99, 99);
}
.topTopBox {
  display: flex;
  justify-content: center;
}

.topArticleBox {
  width: 800px;
}

.theTopBox {
  width: 800px;
  display: flex;
  flex-direction: column;
}
.articleTitle {
  cursor: pointer;
}
.textColor {
  color: rgb(37, 37, 37);
}

.btn-custom {
  background-color: #83C442;
  color: white;
}

.latest-article {
  min-height: 10vh;
  border: 1px solid #BFBFBF;
  border-start-start-radius: 10px;
  border-start-end-radius: 10px;
}

/* 미디엄사이즈 */
@media only screen and (max-width: 768px) {

.topTopBox {
  justify-content:start;
  margin: auto 5px;
}
}

/* 스몰사이즈 */
@media only screen and (max-width: 576px) {

  .theTopBox,
  .topTopBox {
    justify-content:start;
    margin: auto 5px;
  }
}
</style>