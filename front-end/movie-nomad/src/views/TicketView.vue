<template>
  <div>
    <h1>티켓나눔</h1>
  </div>

  <CommunityGrid
    :articles="articles"
  />

  <button @click="goToAddArticle">글쓰기</button>

</template>

<script setup>
import CommunityGrid from '@/components/community/CommunityGrid.vue';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { getArticlesList } from '@/apis/movieApi';

defineProps({
  isDarkMode:Boolean,
})

const router = useRouter()
const articles = ref([])

const goToAddArticle = function () {
  router.push('/create/3/')
}

onMounted(() => {
  getArticlesList()
    .then(response => {
      articles.value = response.data.filter((article) => {
        return article.category === 'ticket'
      })
    })
});
</script>

<style scoped>

</style>