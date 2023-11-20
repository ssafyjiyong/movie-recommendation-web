<template>
  <div>
    <h1>TalkView</h1>
  </div>

  
  <CommunityGrid />

  <button @click="goToAddArticle">글쓰기</button>

</template>

<script setup>
import CommunityGrid from '@/components/community/CommunityGrid.vue';
import { ref, onMounted } from 'vue';
import { useArticleStore } from '@/stores/article';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useArticleStore()
const articles = ref([])

const goToAddArticle = function () {
  router.push('/create/1/')
}



onMounted(() => {
  store.getArticles()
});

</script>

<style scoped>

</style>