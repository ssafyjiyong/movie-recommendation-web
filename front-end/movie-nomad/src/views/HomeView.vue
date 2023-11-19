<template>
  <div>
    <h1>HomeView</h1>
    <form @submit.prevent="searchTheMovie(movieKeyword)">
      <input type="text" v-model="movieKeyword">
      <input type="submit">
    </form>
    <p>test</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movies';

const movieStore = useMovieStore();

const movieKeyword = ref('')
const searchTheMovie = function (movieKeyword) {
  movieStore.searchMovie(movieKeyword)
}

</script>

<style scoped>

</style>