<template>
  <div class="container d-flex justify-content-between my-3">
    <!-- 검색창 및 검색결과 -->
    <div class="col-9 me-3">
      <!-- 검색창 -->
      <div class="searchBox">
        <form @submit.prevent="searchTheMovie">
          <input type="text" v-model="movieKeyword">
          <input type="submit">
        </form>
      </div>

      <!-- 영화리스트 공간 -->
      <div class="movieListBox">
          <MovieCard 
          v-for="searchedMovie in movieStore.searchedMovies" 
          :key="searchedMovie.pk" 
          :searchedMovie="searchedMovie" />
      </div>
    </div>

    <!-- 필터 -->
    <div class="filterBox flex-grow-1">
      <p>필터가 들어갈 자리입니다</p>
    </div>


  </div>
</template>

<script setup>
import MovieCard from '@/components/MovieCard.vue';
import { useMovieStore } from '@/stores/movie';
import { ref } from 'vue';

const movieStore = useMovieStore()
const movieKeyword = ref('')

const searchTheMovie = function () {
  movieStore.searchMovie(movieKeyword.value)
  movieKeyword.value = ''
}

</script>

<style scoped>
.container {
  min-height: 100vh;
}
.filterBox {
  border: 1px solid black;
  border-radius: 10px;
}
.movieListBox {
  border: 1px solid black;
  border-radius: 10px;
}
.searchBox {
  border: 1px solid black;
  margin-bottom: 10px;
}
</style>