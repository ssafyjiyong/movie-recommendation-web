<template>
  <div class="p-2 cursorEffect">

    <div 
    v-if="loading"
    @click="goToDetail"
    class="m-0">
    <div class="spinner-border text-success spinner-border-sm" role="status">
  <span class="visually-hidden">Loading...</span>
</div> 데이터를 불러오는 중입니다</div>

    <div 
    v-else
    @click="goToDetail"
    class="m-0">영화 
    <span class="fw-bold">{{ movieTitle }}</span>
    에 대한 글 <span class="fw-bold">'{{ article.title }}'
    </span></div>

  </div>
  <hr class="m-0">
</template>

<script setup>
import { getMovieDetail } from '@/apis/movieApi';
import { useRouter } from 'vue-router';
import { onMounted, ref } from 'vue';

const router = useRouter()
const movieTitle = ref('')
const props = defineProps({
  article: Object
})
const loading = ref(true)

const goToDetail = function () {
  router.push(`/communitydetail/${props.article.category}/${props.article.id}`)
}

onMounted(() => {
  getMovieDetail(props.article.movie)
    .then((response) => {
      movieTitle.value = response.data['title']
      loading.value = false
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
.cursorEffect {
  cursor: pointer;
}
</style>