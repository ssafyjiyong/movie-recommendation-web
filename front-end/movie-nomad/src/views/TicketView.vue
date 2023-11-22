<template>
  <div>
    <h1>TicketView</h1>
  </div>

  <CommunityGrid
    :articles="ticketArticle"
  />

  <button @click="goToAddArticle">글쓰기</button>

</template>

<script setup>
import CommunityGrid from '@/components/community/CommunityGrid.vue';
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articleStore';
import { useRouter } from 'vue-router';

const router = useRouter()
const articleStore = useArticleStore()
const allArticles = articleStore.articles

const ticketArticle = allArticles.filter((article) => {
  console.log(allArticles)
  return article.category === '나눔'
})

const goToAddArticle = function () {
  router.push('/create/3/')
}



onMounted(() => {
  articleStore.initializeArticles()
});

</script>

<style scoped>

</style>