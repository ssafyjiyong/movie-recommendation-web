<template>
  <div v-if="articleExist">
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

  <div v-else>
    <div id="articleList" class="d-flex text-center justify-content-center">
      <div @click="AddArticle" class="articleTitle p-2">첫번째 글을 작성해보세요!</div>
    </div>
    <hr class="m-0">
  </div>

  <!-- 더 보기 버튼 -->
  <div class="d-flex justify-content-center m-3">
    <button class="btn btn-custom fw-bold" @click="loadMoreArticles">댓글 더 보기</button>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { getArticlesList } from '@/apis/movieApi';


defineProps({
  isDarkMode: Boolean,
  allArticles: Array,
})

const router = useRouter()
const route = useRoute()
const allArticles = ref([])
const articleExist = computed(() => {
  if (paginatedArticles.value.length) {
    return true
  } else {
    return false
  };
})


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

const formatDate = (dateStr) => {
  const date = new Date(dateStr);
  return date.toLocaleDateString('ko-KR', { year: '2-digit', month: '2-digit', day: '2-digit' });
}

const goToDetail = function (articleId) {
  router.push(`/communitydetail/${route.params.category}/${articleId}`)
}

const category = computed(() => {
  if (route.params.category === 'talk') {
    return 1
  } else if (route.params.category === 'toon') {
    return 2
  } else {
    return 3
  }
})

const AddArticle = function () {
  router.push(`/create/${category.value}/`)
}

onMounted(async () => {
  await getArticlesList()
    .then(response => {
      allArticles.value = response.data.filter((article) => {
        return article.category === route.params.category
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

.articleTitle {
  cursor: pointer;
}

.btn-custom {
  background-color: #83C442;
  color: white;
}
</style>