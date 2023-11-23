<template>
  <div class="position-relative" v-if="!loading">

    <!-- 메인 이미지 -->
    <img class="main-background" :src="mainBackground" alt="main-background">

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
        <div class="p-2" v-for="relatedSearch in relatedSearches" :key="relatedSearch.pk">
          <div @click="goToDetail(relatedSearch.pk)">
            <p class="text-black m-0">{{ relatedSearch.title }}</p>
          </div>
        </div>
      </div>

    </div>

    <!-- 커뮤니티 연결 버튼 fixed -->
    <div class="d-flex justify-content-center custom-bottom shake">
      <button @click="goToCommunity" :class="isDarkMode ? 'rounded-btn-dark' : 'rounded-btn'"><span class="fw-bold">{{
        $t('movieStory') }}</span>{{
    $t('letsTalk') }}</button>
    </div>

    <!-- 페이지 소개 메세지 -->
    <div class="text-center infoMsg">
      <h1 class="fw-bold">{{ $t('introduceMsg1') }}</h1>
      <h1 class="fw-bold mb-3">{{ $t('introduceMsg2') }}</h1>
      <h5>{{ $t('introduceMsg3') }}</h5>
      <h5>{{ $t('introduceMsg4') }}</h5>
    </div>

    <!-- 영화 포스터 애니메이션 -->
    <div class="posterTopBox">

      <div class="posterBox1">
        <img v-for="(image, index) in upcomingMovies" :key="index" :src="`${posterUrl}/${image.poster_path}`" alt="index">
      </div>

      <div class="posterBox2">
        <button @click="changTheBackground" type="button" class="btn btn-outline-success btn-custom">눌러보세요</button>
        <img v-for="(image, index) in popularMovies" :key="index" :src="`${posterUrl}/${image.poster_path}`" alt="index">
      </div>

      <div class="posterBox1">
        <img v-for="(image, index) in nowPlayingMovies" :key="index" :src="`${posterUrl}/${image.poster_path}`"
          alt="index">
      </div>

    </div>


    <!-- 자주 묻는 질문 -->
    <div class="qnaGreenBox d-flex justify-content-center align-items-center">

      <div class="qnaBox">
        <h1 class="fw-bold text-center">{{ $t('qna') }}</h1>

        <div class="accordion">
          <div class="accordion-item px-4" @click="toggle(0)">
            <div class="accordion-header d-flex justify-content-between align-items-center">
              <div class="questionFontSize">{{ $t('question1') }}</div>
              <i class="fa-solid fa-angle-down"></i>
            </div>
            <div class="accordion-body" v-show="openIndex === 0">
              <hr>
              <p class="answerFont">{{ $t('answer1') }}</p>
            </div>
          </div>

          <div class="accordion-item px-4" @click="toggle(1)">
            <div class="accordion-header d-flex justify-content-between align-items-center">
              <div class="questionFontSize">{{ $t('question2') }}</div>
              <i class="fa-solid fa-angle-down"></i>
            </div>
            <div class="accordion-body" v-show="openIndex === 1">
              <hr>
              <p class="answerFont">{{ $t('answer2') }}</p>
            </div>
          </div>

          <div class="accordion-item px-4" @click="toggle(2)">
            <div class="accordion-header d-flex justify-content-between align-items-center">
              <div class="questionFontSize">{{ $t('question3') }}</div>
              <i class="fa-solid fa-angle-down"></i>
            </div>
            <div class="accordion-body" v-show="openIndex === 2">
              <hr>
              <p class="answerFont">{{ $t('answer3') }}</p>
            </div>
          </div>

          <div class="accordion-item px-4" @click="toggle(3)">
            <div class="accordion-header d-flex justify-content-between align-items-center">
              <div class="questionFontSize">{{ $t('question4') }}</div>
              <i class="fa-solid fa-angle-down"></i>
            </div>
            <div class="accordion-body" v-show="openIndex === 3">
              <hr>
              <p class="answerFont">{{ $t('answer4') }}</p>
            </div>
          </div>

          <div class="accordion-item px-4" @click="toggle(4)">
            <div class="accordion-header d-flex justify-content-between align-items-center">
              <div class="questionFontSize">{{ $t('question5') }}</div>
              <i class="fa-solid fa-angle-down"></i>
            </div>
            <div class="accordion-body" v-show="openIndex === 4">
              <hr>
              <p class="answerFont">{{ $t('answer5') }}</p>
            </div>
          </div>
        </div>

      </div>
    </div>


  </div>


  <!-- 로딩중에 나오는 명대사 -->
  <div v-else class="d-flex justify-content-center align-items-center m-5">
    <div class="spinner-border text-success d-inline" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
    <h3 class="m-3">이스터에그를 찾아보세요!</h3>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import { useMovieStore } from '@/stores/movieStore';
import { useUserStore } from '@/stores/userStore';
import { useRouter } from 'vue-router'
import { getPopularMovies, getUpcomingMovies, getNowPlayingMovies } from '@/apis/movieApi'
import { debounce } from 'lodash';

const userStore = useUserStore()

// token 값이 변경될 때마다 실행
watch(() => userStore.nickname, () => {
  if (userStore.nickname !== "") {
    location.reload()
  }
});


defineProps({
  isDarkMode: Boolean,
})

const mainBackground = ref('src/images/main_background.jpg')
const changTheBackground = function () {
  mainBackground.value = 'src/images/main_background.gif'
}

const router = useRouter()
const movieStore = useMovieStore();
const movieKeyword = ref('')

// 로딩중
const loading = ref(true)

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
  return movieStore.searchedMovies.slice(0, 7)
})

const searchMovie = function () {
  movieStore.searchTheMovie(movieKeyword.value)
  router.push('/movies')
}

const searchMovieForRelatedSearches = function () {
  movieStore.searchTheMovie(movieKeyword.value)
}

const debouncedSearch = debounce(searchMovieForRelatedSearches, 100);

const goToDetail = function (moviePk) {
  router.push(`moviedetail/${moviePk}/`)
}

const clearPlaceholder = function () {
  placeholderText.value = ''
  isFocused.value = true
}

const restorePlaceholder = function () {
  setTimeout(() => {
    placeholderText.value = 'MOVIE NOMAD'
    isFocused.value = false
  }, 200)
}

const goToCommunity = function () {
  router.push('/community/talk')
}


const openIndex = ref(null)

// toggle 함수 수정
const toggle = (index => {
  if (openIndex.value === index) {
    openIndex.value = null
  } else {
    openIndex.value = index
  }
})


onMounted(() => {
  movieStore.initializeMovies(),
    getPopularMovies()
      .then((response) => {
        popularMovies.value = Array(5).fill(response.data.results).flat();
        loading.value = false
      })
      .catch((error) => {
        console.error('Error getPopularMovies:', error)
      });
  getUpcomingMovies()
    .then((response) => {
      upcomingMovies.value = Array(5).fill(response.data.results).flat();
    })
    .catch((error) => {
      console.error('Error getUpcomingMovies:', error)
    });
  getNowPlayingMovies()
    .then((response) => {
      nowPlayingMovies.value = Array(5).fill(response.data.results).flat();
    })
    .catch((error) => {
      console.error('Error getNowPlayingMovies:', error)
    });
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

.infoMsg {
  margin-top: 7vh;
  margin-bottom: 5vh;
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

.rounded-btn-dark {
  padding: 11px 20px;
  border: 0;
  border-radius: 30px;
  background-color: green;
  color: white;
  width: 400px;
}

.posterBox1 {
  display: flex;
  animation: scroll1 250s linear infinite;
  width: max-content;
}

.posterBox2 {
  display: flex;
  animation: scroll2 250s linear infinite;
  width: max-content;
}

.posterBox1 img,
.posterBox2 img,
.btn-custom {
  width: 20vh;
  padding: 10px;
}


.posterTopBox {
  max-width: 100vw;
  overflow: hidden;
}

.qnaGreenBox {
  height: auto;
  background-color: #92DE4A;
  padding: 7vh;
  font-family: 'Nanum Gothic', sans-serif;
  margin-top: 3vh;
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

@keyframes scroll1 {
  0% {
    transform: translateX(0%);
  }

  100% {
    transform: translateX(-70%);
  }
}

@keyframes scroll2 {
  0% {
    transform: translateX(-70%);
  }

  100% {
    transform: translateX(9%);
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
