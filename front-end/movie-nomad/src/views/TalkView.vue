<template>
  <div>
    <h1>TalkView</h1>
  </div>
  <CommunityGrid :articles="articles" />
  <button @click="goToAddArticle">글쓰기</button>
</template>

<script setup>
import CommunityGrid from '@/components/community/CommunityGrid.vue';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { getArticlesList } from '@/apis/movieApi';

const router = useRouter()
const articles = ref([])

const goToAddArticle = function () {
  router.push('/create/1/')
}

onMounted(() => {
  getArticlesList()
    .then(response => {
      articles.value = response.data.filter((article) => {
        return article.category === '수다'
      })
    })
});

</script>

<style scoped></style>