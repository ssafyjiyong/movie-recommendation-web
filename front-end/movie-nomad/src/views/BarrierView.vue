<template>
  <div>
    <h1>BarrierView</h1>
  </div>

  <CommunityGrid
    :articles="articleStore.articles"
  />


</template>

<script setup>
import CommunityGrid from '@/components/community/CommunityGrid.vue';
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articleStore';

const articleStore = useArticleStore()


onMounted(() => {
  articleStore.initializeArticles()
});

</script>

<style scoped>

</style>