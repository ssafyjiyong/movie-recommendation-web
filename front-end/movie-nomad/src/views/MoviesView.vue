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
          v-for="(searchedMovie, idx) in searchedMovies?.slice(pageStartIdx, pageStartIdx + ITEM_PER_PAGE)"
          :key="idx"
          :searchedMovie="searchedMovie" />
      </div>

      <Pagination 
      :list="searchedMovies" 
      v-bind="{ ITEM_PER_PAGE, PAGE_PER_SECTION }" 
      @change-page="onChangePage" />

    </div>

    <!-- 필터 -->
    <div class="filterBox flex-grow-1">
      <p>필터가 들어갈 자리입니다</p>
    </div>


  </div>
</template>


<script setup>
import MovieCard from '@/components/MovieCard.vue';
import { ref, computed } from 'vue';
import { searchMovie } from '@/apis/movieApi'
import Pagination from '@/components/Pagination.vue';

const movieKeyword = ref('')
const searchedMovies = ref([])

const searchTheMovie = () => {
  searchMovie(movieKeyword.value)
  .then((response) => {
    if (response && response.data) {
      searchedMovies.value = response.data
      movieKeyword.value = ''
      }
    })
    .catch((error) => {
      console.error('Error search the movie', error)
    })
}

// 디버깅을 위해 위의 방식 채택
// const searchTheMovie = function () {
//   searchMovie(movieKeyword.value)
//   movieKeyword.value = ''
// }


// 아래는 페이지네이션 관련 코드
const articles = new Array(111);
for (let i = 0; i < articles.length; i++) {
  articles[i] = `Article ${i + 1}`;
}

const ITEM_PER_PAGE = ref(10);
const PAGE_PER_SECTION = ref(5);
let curPage = ref(1);

const pageStartIdx = computed(() => {
  return (curPage.value - 1) * ITEM_PER_PAGE.value;
});

const onChangePage = (data) => {
  curPage.value = data;
};

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