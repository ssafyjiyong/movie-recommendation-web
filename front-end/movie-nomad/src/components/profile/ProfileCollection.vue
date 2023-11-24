<template>
  <div class="d-flex justify-content-center">
  <div class="border w-75 rounded-3 my-2 minLimit">


    <div v-if="!loading">
    <div>'{{ collection.name }}' 컬렉션</div>
    <div class="d-flex justify-content-center">
    <div class="topBox d-flex flex-column">
      <div class="firstLine row">
        <div class="left1 col-6 p-0">
          <img v-if="movies[0]" :src="`https://image.tmdb.org/t/p/w500${movies[0].poster_path}`" alt="movie_poster1">
        </div>
        <div class="right1 col-6 p-0">
          <img v-if="movies[1]" :src="`https://image.tmdb.org/t/p/w500${movies[1].poster_path}`" alt="movie_poster1">
        </div>
      </div>
      
      <div class="secondLine row mb-2">
        <div class="left2 col-6 p-0">
          <img v-if="movies[2]" :src="`https://image.tmdb.org/t/p/w500${movies[2].poster_path}`" alt="movie_poster1">
        </div>
        <div class="right2 col-6 p-0">
          <img v-if="movies[3]" :src="`https://image.tmdb.org/t/p/w500${movies[3].poster_path}`" alt="movie_poster1">
        </div>
      </div>
    </div>
  </div>
</div>

<div v-else>
  <div class="spinner-border text-success spinner-border-sm" role="status">
  <span class="visually-hidden">Loading...</span>
  </div>
  <p>컬렉션을 확인중입니다</p>
</div>


  </div>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getMoviesList } from '@/apis/movieApi';

const props = defineProps({
  collection: Object
})

const movies = ref([])
const loading = ref(true)

onMounted(() => {
  getMoviesList()
    .then(response => {
      props.collection.movie.slice(0, 4).forEach(pk => {
        const movie = response.data.find(movie => movie.pk === pk);
        // console.log(movie);
        if (movie) {
          movies.value.push(movie);
          loading.value = false
        }
      });
    })
})

</script>

<style scoped>
.minLimit {
  min-width: 180px;
}
img {
  height: 13vh;
}
</style>