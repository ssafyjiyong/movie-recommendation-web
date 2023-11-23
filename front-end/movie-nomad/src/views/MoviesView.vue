<template>
  <div class="container d-flex justify-content-between my-3 text-black" v-if="!movieStore.loading">
    <!-- 검색창 및 검색결과 -->
    <div class="col-9 me-3">

      <!-- 영화 검색창 -->
      <div class="d-flex justify-content-center mb-3">
        <form @submit.prevent="searchMovie"
          :class='["rounded-3", "border", isFocused ? "search-form-focus" : "search-form-nofocus"]'>
          <input @keyup="debouncedSearch" 
          type="text" class="search-input" 
          :placeholder=placeholderText
          :value="movieKeyword" 
          @click="resetFilteredMovies"
          @input="movieKeyword = $event.target.value"
          @focus="clearPlaceholder"
          @blur="restorePlaceholder">
          <button type="submit" class="btn btn-link text-black"><i class="fa-solid fa-magnifying-glass"></i></button>
        </form>
      </div>

      <!-- 영화리스트 공간 -->
      <div class="border rounded-3">
        <div class="filterTitleBoxTop text-white p-2 m-0">
          <p class="fw-bold m-0 fs-5">영화목록</p>
        </div>

        <div class="p-1 movieListBox">

            <div v-if="paginatedMovies.length">
              <div v-for="(searchedMovie, idx) in paginatedMovies" :key="idx">
                <MovieCard :searchedMovie="searchedMovie" />
                <hr class="m-0">
              </div>
            </div>
            <div v-else class="text-center pt-2">
              <i class="fa-solid fa-circle-exclamation text-secondary fa-lg"></i>
              <h4 class="p-2 fw-bold text-secondary">검색어에 해당하는 결과가 없습니다</h4>
            </div>

        </div>
        <!-- 더 보기 버튼 -->
        <div class="d-flex justify-content-center">
          <button class="btn btn-custom fw-bold m-2" @click="loadMoreMovies">결과 더 보기</button>
        </div>
      </div>

    </div>


    <!-- 필터 -->
    <div class="border rounded-3 flex-grow-1">

      <div class="filterTitleBoxTop text-white p-2">
        <p class="fw-bold m-0">장르별: </p>
      </div>
      <div class="mb-2">
        <button @click="resetFilteredMovies" class="btn btn-outline-success btn-sm m-1">전체</button>
        <button v-for="(genre, idx) in genres" @click="filterGenre(genre.name)" :key="idx" type="button"
          class="btn btn-outline-success btn-sm m-1">
          {{ genreTranslation[genre.name] }}
        </button>
      </div>

      <div class="filterTitleBox text-white p-2">
        <p class="fw-bold m-0">분류별: </p>
      </div>
      <div class="mb-2">
        <button @click="popularity" class="btn btn-outline-success btn-sm m-1">인기도</button>
        <button @click="voteAverage" class="btn btn-outline-success btn-sm m-1">평점</button>
        <button @click="voteCount" class="btn btn-outline-success btn-sm m-1">평가수</button>
        <button @click="latest" class="btn btn-outline-success btn-sm m-1">최신</button>
        <button @click="classic" class="btn btn-outline-success btn-sm m-1">오래된</button>
      </div>

      <div class="filterTitleBox text-white p-2">
        <p class="fw-bold m-0">원어별: </p>
      </div>
      <div class="mb-2">
        <button @click="english" class="btn btn-outline-success btn-sm m-1">영어</button>
        <button @click="korean" class="btn btn-outline-success btn-sm m-1">한국어</button>
        <button @click="spanish" class="btn btn-outline-success btn-sm m-1">스페인어</button>
        <button @click="japanease" class="btn btn-outline-success btn-sm m-1">일본어</button>
        <button @click="chinease" class="btn btn-outline-success btn-sm m-1">중국어</button>
        <button @click="hongkong" class="btn btn-outline-success btn-sm m-1">광동어</button>
        <button @click="russian" class="btn btn-outline-success btn-sm m-1">러시아어</button>
        <button @click="franch" class="btn btn-outline-success btn-sm m-1">프랑스어</button>
        <button @click="hindi" class="btn btn-outline-success btn-sm m-1">힌디어</button>
      </div>


    </div>
  </div>

  <div v-else class="d-flex justify-content-center align-items-center m-5">
    <div class="spinner-border text-success d-inline" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
    <h3 class="m-3">{{ randomMessage }}</h3>
  </div>
</template>


<script setup>
import MovieCard from '@/components/MovieCard.vue';
import { ref, onMounted, computed } from 'vue';
import { useMovieStore } from '@/stores/movieStore';
import { debounce } from 'lodash';
import { getGenres } from '@/apis/movieApi'

const movieStore = useMovieStore()
const movieKeyword = ref('')

// 검색창 관련 변수
const placeholderText = ref('원하시는 영화를 검색해보세요!')
const isFocused = ref(false)

const searchMovieForRelatedSearches = function () {
  movieStore.searchTheMovie(movieKeyword.value)
}

const debouncedSearch = debounce(searchMovieForRelatedSearches, 100);

const clearPlaceholder = function () {
  placeholderText.value = ''
  isFocused.value = true
}

const restorePlaceholder = function () {
  setTimeout(() => {
    placeholderText.value = '원하시는 영화를 검색해보세요!'
    isFocused.value = false
  }, 200)
}

// 로딩 관련
const randomMessage = movieStore.loadingMessage[Math.floor(Math.random() * movieStore.loadingMessage.length)];

const searchMovie = function () {
  movieStore.searchTheMovie(movieKeyword.value)
}

// 페이지 상태 관리
const itemsPerPage = 15
const page = ref(1)

// 페이지에 따라 영화 데이터 범위 조정(최초 첫 번째 페이지 데이터 로드)
const paginatedMovies = computed(() => {
  if (filteredMovies.value.length) {
    return filteredMovies.value.slice(0, end.value)
  } else {
    return movieStore.searchedMovies.slice(0, end.value)
  }
})

const start = ref(0)
const end = ref(14)
// 더 보기 버튼 클릭 시 페이지 상태 증가
const loadMoreMovies = () => {
  start.value = page.value * itemsPerPage
  end.value = start.value + itemsPerPage
  page.value++
}

//////////////////////////////////필터/////////////////////////////////////////

const filteredMovies = ref([]);

const resetFilteredMovies = () => {
  filteredMovies.value = [];
}

const filterGenre = (genre) => {
  filteredMovies.value = movieStore.searchedMovies.filter(movie =>
    movie.genres.some(g => g.name === genre)
  );
}

const popularity = () => {
  resetFilteredMovies();
  return movieStore.searchedMovies.sort((a, b) => {
    return b.popularity - a.popularity
  })
}

const voteAverage = () => {
  resetFilteredMovies();
  return movieStore.searchedMovies.sort((a, b) => {
    return b.vote_average - a.vote_average
  })
}

const voteCount = () => {
  resetFilteredMovies();
  return movieStore.searchedMovies.sort((a, b) => {
    return b.vote_count - a.vote_count
  })
}

const latest = () => {
  resetFilteredMovies();
  return movieStore.searchedMovies.sort((a, b) => {
    return b.release_date > a.release_date ? 1 : -1
  })
}

const classic = () => {
  filteredMovies.value = movieStore.searchedMovies.filter(movie => movie.release_date !== '').sort((a, b) => {
    return b.release_date > a.release_date ? -1 : 1
  })
}

const english = () => {
  filteredMovies.value = movieStore.searchedMovies.filter(movie => movie.original_language === "en")

}

const korean = () => {
  filteredMovies.value = movieStore.searchedMovies.filter(movie => movie.original_language === "ko")
}

const spanish = () => {
  filteredMovies.value = movieStore.searchedMovies.filter(movie => movie.original_language === "es")
}

const japanease = () => {
  filteredMovies.value = movieStore.searchedMovies.filter(movie => movie.original_language === "ja")
}

const chinease = () => {
  filteredMovies.value = movieStore.searchedMovies.filter(movie => movie.original_language === "zh")
}

const hongkong = () => {
  filteredMovies.value = movieStore.searchedMovies.filter(movie => movie.original_language === "yue")
}

const russian = () => {
  filteredMovies.value = movieStore.searchedMovies.filter(movie => movie.original_language === "ru")
}

const franch = () => {
  filteredMovies.value = movieStore.searchedMovies.filter(movie => movie.original_language === "fr")
}

const hindi = () => {
  filteredMovies.value = movieStore.searchedMovies.filter(movie => movie.original_language === "hi")
}

const genres = ref([])

const genreTranslation = {
  'Action': '액션',
  'Adventure': '모험',
  'Animation': '애니메이션',
  'Comedy': '코미디',
  'Crime': '범죄',
  'Documentary': '다큐멘터리',
  'Drama': '드라마',
  'Family': '가족',
  'Fantasy': '판타지',
  'History': '역사',
  'Horror': '공포',
  'Music': '음악',
  'Mystery': '미스터리',
  'Romance': '멜로/로맨스',
  'Science Fiction': 'SF',
  'TV Movie': 'TV 영화',
  'Thriller': '스릴러',
  'War': '전쟁',
  'Western': '서부'
}

onMounted(() => {
  movieStore.initializeMovies();
  getGenres()
    .then((response) => {
      genres.value = response.data
    })
    .catch((error) => {
      console.error('Error getting all genres:', error)
    });
});

</script>


<style scoped>
.btn-custom {
  background-color: #83C442;
  color: white;
}

.movieListBox {
  background-color: #F6FFE8;
}

.filterTitleBoxTop {
  background-color: #83C442;
  border-top-right-radius: 0.5rem;
  border-top-left-radius: 0.5rem;
  margin-bottom: 5px;
}

.filterTitleBox {
  background-color: #83C442;
  margin-bottom: 5px;
}

.container {
  min-height: 100vh;
}

.searchBox {
  border: 1px solid black;
  margin-bottom: 10px;
}

.search-form-nofocus {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  background-color: white;
  padding: 7px;
  /* box-shadow: 0 4px 6px 0 hsla(0, 0%, 32%, 0.2); */
}

.search-form-focus {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  background-color: white;
  padding: 7px;
}

.search-input {
  width: 90%;
  border: none;
  padding-top: 5px;
  padding-left: 10px;
}

.search-input:focus {
  outline: none;
}

.search-input::placeholder {
  text-align: center;
  font-weight: bold;
  color: #7DBE3F;
  font-size: 1.3em;
  opacity: 0.7;
}
</style>