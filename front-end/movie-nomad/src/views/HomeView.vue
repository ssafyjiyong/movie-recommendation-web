<template>
  <div class="position-relative">

    <!-- 메인 이미지 -->
    <img class="main-background" src="@/images/main_background.gif" alt="main-background">

    <!-- 영화 검색창 absolute -->
    <div class="d-flex justify-content-center position-absolute custom-top start-50 translate-middle">
      <form @submit.prevent="searchMovie" :class='isFocused ? "search-form-focus" : "search-form-nofocus"'>
    <button v-if="!isFocused" type="submit" class="btn btn-link text-black">
      <i class="fa-solid fa-magnifying-glass"></i></button>
    <input @keyup="debouncedSearch" type="text" class="search-input" :placeholder=placeholderText
      :value="movieKeyword" @input="movieKeyword = $event.target.value" @focus="clearPlaceholder"
      @blur="restorePlaceholder">
    <button v-if="isFocused" type="submit" class="btn btn-link text-black"><i
        class="fa-solid fa-magnifying-glass"></i></button>
  </form>

      <!-- 관련 검색어 -->
      <div class="related-searches" v-if="isFocused">
        <div class="p-2" v-for="relatedSearch in relatedSearches" :key="relatedSearch">{{ relatedSearch }}</div>
      </div>

    </div>

    <!-- 커뮤니티 연결 버튼 fixed -->
    <div class="d-flex justify-content-center custom-bottom shake">
      <button @click="goToCommunity" class="rounded-btn"><span class="fw-bold">영화 이야기</span> 나누러 가기</button>
    </div>

    <!-- 영화 포스터 애니메이션 -->
    <div class="posterTopBox">

      <div class="posterBox">
        <img v-for="(image, index) in upcomingMovies" :key="index" 
        :src="`${posterUrl}/${image.poster_path}`" alt="index">
      </div>

      <div class="posterBox">
        <img v-for="(image, index) in nowPlayingMovies" :key="index" 
        :src="`${posterUrl}/${image.poster_path}`" alt="index">
      </div>

      <div class="posterBox">
        <img v-for="(image, index) in popularMovies" :key="index" 
        :src="`${posterUrl}/${image.poster_path}`" alt="index">
      </div>

    </div>


    <!-- 자주 묻는 질문 -->
    <div class="qnaGreenBox d-flex justify-content-center align-items-center">

      <div class="qnaBox">
        <h1 class="fw-bold text-center">자주 묻는 질문</h1>

        <div class="accordion" v-for="(qna, index) in qnas" :key="index">
          <div class="accordion-item px-4" @click="toggle(index)">
            <div class="accordion-header d-flex justify-content-between align-items-center">
              <div class="questionFontSize">{{ qna.question }}</div>
              <i class="fa-solid fa-angle-down"></i>
            </div>
            <div class="accordion-body" v-show="qna.open">
              <hr>
              <p class="answerFont">{{ qna.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>


  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import { useMovieStore } from '@/stores/movieStore';
import { useRouter } from 'vue-router'
import { getPopularMovies, getUpcomingMovies, getNowPlayingMovies } from '@/apis/movieApi'
import { debounce } from 'lodash';

const router = useRouter()
const movieStore = useMovieStore();
const movieKeyword = ref('')

// 포스터 관련 변수
const popularMovies = ref([])
const upcomingMovies = ref([])
const nowPlayingMovies = ref([])
const posterUrl = 'https://image.tmdb.org/t/p/w500';

// 검색창 관련 변수
const placeholderText = ref('MOVIE NOMAD')
const isFocused = ref(false)
const relatedSearches = computed(() => {
  // 키워드 써칭하여 결과는 최대 7개만
  return movieStore.searchedMovies
    .map(movie => movie.title)
    .slice(0, 7)
})

const searchMovie = function () {
  movieStore.searchTheMovie(movieKeyword.value)
  router.push('/movies')
}

const searchMovieForRelatedSearches = function () {
  movieStore.searchTheMovie(movieKeyword.value)
}

const debouncedSearch = debounce(searchMovieForRelatedSearches, 300);

const clearPlaceholder = function () {
  placeholderText.value = ''
  isFocused.value = true
}

const restorePlaceholder = function () {
  placeholderText.value = 'MOVIE NOMAD'
  isFocused.value = false
}

const goToCommunity = function () {
  router.push('/talk')
}

// QnA 관련 스크립트
const qnas = ref([
  { question: '단축키 모드는 무엇인가요?', answer: '단축키 모드는 마우스를 사용하지 않고도 사이트를 조작할 수 있는 편리한 모드입니다. 안내 팝업창을 확인해주세요!', open: false },
  { question: '서비스 사용료가 있나요?', answer: '해당 서비스는 무료로 제공되고 있습니다. 우측 하단에 커피 버튼을 누르시면 저희가 커피를 한 잔 할 수 있습니다 :) 감사합니다!', open: false },
  { question: '어떤 기기에서 사용할 수 있나요?', answer: '저희 서비스는 모바일과 인터넷 모두에서 사용 가능합니다.', open: false },
  { question: 'Team M.A.D에 대해 알려주세요.', answer: 'M.A.D는 Making A Difference의 약자로, 작은 변화로 사회에 기여하는 것을 목표로 하고 있습니다.', open: false }
])

const toggle = index => {
  qnas.value[index].open = !qnas.value[index].open
}

onMounted(() => {
  movieStore.initializeMovies(),
    getPopularMovies()
      .then((response) => {
        popularMovies.value = response.data.results
      })
      .catch((error) => {
        console.error('Error getPopularMovies:', error)
      }),
    getUpcomingMovies()
      .then((response) => {
        upcomingMovies.value = response.data.results
      })
      .catch((error) => {
        console.error('Error getUpcomingMovies:', error)
      }),
    getNowPlayingMovies()
      .then((response) => {
        nowPlayingMovies.value = response.data.results
      })
      .catch((error) => {
        console.error('Error getNowPlayingMovies:', error)
      })
});

</script>

<style scoped>
.accordion-item {
  width: 80vw;
  border-radius: 25px;
  margin: 15px;
  padding-top: 10px;
  padding-bottom: 10px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.accordion-body {
  padding: 0;
}

.main-background {
  width: 100%;
  height: 70vh;
  opacity: 0.85;
  object-fit: cover;
  margin-bottom: 3vh;
}

.custom-top {
  top: 25vh !important;
}

.custom-bottom {
  position: fixed;
  bottom: 70px;
  width: 100%;
  z-index: 5;
}

.search-form-nofocus {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 70vw;
  background-color: white;
  border-radius: 50px;
  padding: 10px;
  box-shadow: 0 4px 6px 0 hsla(0, 0%, 32%, 0.2);
}

.search-form-focus {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 70vw;
  background-color: white;
  border-start-start-radius: 30px;
  border-start-end-radius: 30px;
  padding: 10px;
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
  font-size: 1.5em;
  opacity: 0.7;
}

.related-searches {
  position: absolute;
  top: 95%;
  width: 100%;
  background: white;
  padding: 10px;
  border-end-start-radius: 30px;
  border-end-end-radius: 30px;
}

.related-searches div:hover {
  background-color: #f2f2f2;
}

.rounded-btn {
  padding: 11px 20px;
  border: 0;
  border-radius: 30px;
  background-color: rgb(32, 32, 32);
  color: white;
  width: 400px;
}

.posterBox {
  display: flex;
}


.posterBox img {
  width: 20vh;
  padding: 10px;
}

.posterTopBox {
  max-width: 80vw;
}

.qnaGreenBox {
  height: auto;
  background-color: #92DE4A;
  padding: 30px;
  font-family: 'Nanum Gothic', sans-serif
}

.questionFontSize {
  font-size: large;
  font-weight: bold;
  color: rgb(68, 68, 68);
}

.shake {
  animation: shake 2.05s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
  transform: translate3d(0, 0, 0);
  animation-iteration-count: infinite;
}

@keyframes shake {

  10%,
  90% {
    transform: translate3d(0, -3px, 0);
  }

  20%,
  80% {
    transform: translate3d(0, 2px, 0);
  }
}

@media (max-width: 565px) {

  .search-form-nofocus,
  .search-form-focus {
    width: 90vw;
  }

  .rounded-btn {
    width: 60%;
  }
}

@media (max-width: 385px) {
  .rounded-btn {
    width: 90%;
  }
}
</style>
