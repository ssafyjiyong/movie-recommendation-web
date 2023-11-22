<template>
  <div>
    <RouterLink class="box" :to="{ name: 'communityDetail', params: { articleId: article.id } }">
      <div>{{ article.title }}</div>
      <div>{{ movieTitle }}</div>
    </RouterLink>
  </div>
</template>

<script setup>
import { getMovieDetail } from '@/apis/movieApi';
import { RouterLink } from 'vue-router';
import { onMounted, ref } from 'vue';

const movieTitle = ref('')
const props = defineProps({
  article: Object
})

onMounted(() => {
  getMovieDetail(props.article.movie)
    .then((response) => {
      // console.log(response.data['title'])
      movieTitle.value = response.data['title']
    })
})
</script>

<style scoped>
.box {
  padding: 0 5%;
  margin: 1% 0;
  display: flex;
  justify-content: space-between;
}
</style>