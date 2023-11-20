<template>
  <div>
    <h1>TalkView</h1>
  </div>

  
  <ArticleListCard />

  <button>글쓰기</button>

</template>

<script setup>
import ArticleListCard from '@/components/ArticleListCard.vue';
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/article';

const store = useArticleStore()


onMounted(() => {
  store.initializeArticles()
});

</script>

<style scoped>

</style>