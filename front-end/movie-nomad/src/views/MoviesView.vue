<template>
  <div class="container d-flex justify-content-between my-3">
    <!-- 검색창 및 검색결과 -->
    <div class="col-9 me-3">
      <!-- 검색창 -->
      <div class="searchBox">
        <form @submit.prevent="searchMovie">
          <input type="text" v-model="movieKeyword">
          <input type="submit">
        </form>
      </div>

      <!-- 영화리스트 공간 -->
      <div class="movieListBox">
        <MovieCard v-for="(searchedMovie, idx) in paginatedMovies" 
        :key="idx" :searchedMovie="searchedMovie" />
      </div>

      <!-- 더 보기 버튼 -->
      <button @click="loadMoreMovies">더 보기</button>
    </div>


    <!-- 필터 -->
    <div class="filterBox flex-grow-1">
      <p>필터가 들어갈 자리입니다</p>
    </div>

  </div>

  <!-- <div v-else>
    <div class="spinner-border text-success" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
    <span>영화 목록을 가져오는중...</span>
  </div> -->
</template>


<script setup>
import MovieCard from '@/components/MovieCard.vue';
import { ref, onMounted } from 'vue';
import { useMovieStore } from '@/stores/movieStore';

const movieStore = useMovieStore()
const movieKeyword = ref('')
const loading = ref(true) // 로딩 상태 관리

const searchMovie = function () {
  movieStore.searchTheMovie(movieKeyword.value)
  paginatedMovies.value = movieStore.searchedMovies.slice(0, itemsPerPage)
}

// 페이지 상태 관리
const itemsPerPage = 15
const page = ref(1)

// 페이지에 따라 영화 데이터 범위 조정(최초 첫 번째 페이지 데이터 로드)
const paginatedMovies = ref(movieStore.searchedMovies.slice(0, 14))

// 더 보기 버튼 클릭 시 페이지 상태 증가
const loadMoreMovies = () => {
  const start = page.value * itemsPerPage
  const end = start + itemsPerPage
  paginatedMovies.value = movieStore.searchedMovies.slice(0, end)
  page.value++
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