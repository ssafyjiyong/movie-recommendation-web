<template>
  <div class="box col-8">
    <div class="collection-name">{{ collection.name }}</div>
    <div
      class="col-6"
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
.collection-name {
  width: 100%;
  text-align: center;
}
.box {
  display: flex;
  flex-wrap: wrap;  
}

.box img{
  justify-content: center;
  width: 80%;
}
</style>