<template>
  <div>
    <h1>ToonView</h1>
  </div>

  <CommunityGrid
    :articles="toonArticle"
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

const toonArticle = allArticles.filter((article) => {
  console.log(allArticles)
  return article.category === '영화툰'
})

const goToAddArticle = function () {
  router.push('/create/2/')
}



onMounted(() => {
  articleStore.initializeArticles()
});

</script>

<style scoped>

</style>