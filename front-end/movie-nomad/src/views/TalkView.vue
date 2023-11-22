<template>
  <div class="d-flex justify-content-center">
    <div class="d-flex flex-column theTopBox">
      <div class="m-3">
        <i class="fa-solid fa-comment-dots fa-lg mx-2"></i><span class="fw-bold textColor">영화토크</span>
      </div>

        <div class="topArticleBox">
          <div class="latest-article">
            <div v-for="article in displayedarticles" :key="article.id">
              <div class="articleBox d-flex justify-content-between">
                <div>{{ article.id }}</div>
                <div>{{ article.title }}</div>
                <div>{{ article.user.nickname }}</div>
                <div>{{ formatDate(article.created_at) }}</div>
              </div>
            </div>
            <button @click="goToAddArticle">글쓰기</button>
          </div>
        </div>

      <!-- 페이지네이션 -->
      <div>
        <button v-for="n in pageCount" :key="n" @click="changePage(n)">
          {{ n }}
        </button>
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
const currentPage = ref(1)
const articlesPerPage = 15

const displayedarticles = computed(() => {
  const start = (currentPage.value - 1) * articlesPerPage;
  const end = start + articlesPerPage;
  return allArticles.value.slice(start, end);
});

const pageCount = computed(() => Math.ceil(allArticles.value.length / articlesPerPage));

const changePage = (page) => {
  currentPage.value = page;
};

const goToAddArticle = function () {
  router.push('/create/1/')
}

const formatDate = (dateStr) => {
  const date = new Date(dateStr);
  return date.toLocaleDateString('ko-KR', { year: '2-digit', month: '2-digit', day: '2-digit' });
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
.topArticleBox,
.theTopBox {
  width: 800px;
}

.textColor {
  color: rgb(37, 37, 37);
}

.latest-article {
  height: 80vh;
  border: 1px solid black;
}

.articleBox {
  border: 1px solid black;
}</style>