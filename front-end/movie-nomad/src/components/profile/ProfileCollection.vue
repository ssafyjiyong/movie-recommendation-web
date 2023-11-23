<template>
  <div class="box">
    <div
      v-for="movie in movies"
      :key="movie.id"
    >
      <img
      :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" 
      alt="movie_poster"
      >
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getMoviesList } from '@/apis/movieApi';
import { useMovieStore } from '@/stores/movieStore';

const movieStore = useMovieStore()
const props = defineProps({
  collection: Object
})

const movies = ref([])

onMounted( () => {
  getMoviesList()
  .then(response => {
    props.collection.movie.slice(0, 4).forEach(pk => {
        const movie = response.data.find(movie => movie.pk === pk);
        // console.log(movie);
        if(movie) {
          movies.value.push(movie);
        }
      });
  })
})

</script>

<style scoped>
.box {
  display: flex;
  flex-wrap: wrap;
}

.box img{
  width: 25%;
}
</style>