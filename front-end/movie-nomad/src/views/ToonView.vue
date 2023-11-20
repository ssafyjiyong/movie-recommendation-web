<template>
  <div>
    <h1>ToonView</h1>
  </div>

  <ArticleListCard />

<button @click="goToAddArticle">글쓰기</button>

</template>

<script setup>
import ArticleListCard from '@/components/ArticleListCard.vue';
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/article';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useArticleStore()

const goToAddArticle = function () {
  router.push('/create/2/')
}

onMounted(() => {
  store.getArticles()
});

</script>

<style scoped>

</style>