<template>
  <div class="position-relative">

    <!-- 메인 이미지 -->
    <img class="main-background" src="@/images/main_background.jpg" alt="main-background">

    <!-- 영화 검색창 absolute -->
    <div class="d-flex justify-content-center position-absolute custom-top start-50 translate-middle">
      <form @submit.prevent="searchTheMovie(movieKeyword)"
        :class='isFocused ? "search-form-focus" : "search-form-nofocus"'>
        <button v-if="!isFocused" type="submit" class="btn btn-link text-black"><i
            class="fa-solid fa-magnifying-glass"></i></button>
        <input type="text" v-model="movieKeyword" class="search-input" :placeholder=placeholderText
          @focus="clearPlaceholder" @blur="restorePlaceholder">
        <button v-if="isFocused" type="submit" class="btn btn-link text-black"><i
            class="fa-solid fa-magnifying-glass"></i></button>
      </form>

      <div class="related-searches" v-if="isFocused">
        <div class="p-2" v-for="relatedSearch in relatedSearches" :key="relatedSearch">{{ relatedSearch }}</div>
      </div>

    </div>

    <!-- 커뮤니티 연결 버튼 fixed -->
    <div class="d-flex justify-content-center custom-bottom">
      <button class="rounded-btn"><span class="fw-bold">영화 이야기</span> 나누러 가기</button>
    </div>

    <!-- 영화 포스터 애니메이션 -->
    <div class="posterBox">

    </div>

    <!-- 자주 묻는 질문 -->
    <div class="qnaBox d-flex-column justify-content-center">
      <h1 class="fw-bold">자주 묻는 질문</h1>

      <div class="accordion" v-for="(qna, index) in qnas" :key="index">
        <div class="accordion-header" @click="toggle(index)">
          <h2>{{ qna.question }}</h2>
        </div>
        <div class="accordion-body" v-show="qna.open">
          <p>{{ qna.answer }}</p>
        </div>
      </div>
    </div>


  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';

const movieStore = useMovieStore();

const movieKeyword = ref('')
const searchTheMovie = function (movieKeyword) {
  movieStore.searchMovie(movieKeyword)
}

const placeholderText = ref('MOVIE NOMAD')
const isFocused = ref(false)
const relatedSearches = ref(['관련 검색어 1', '관련 검색어 2', '관련 검색어 3'])

const clearPlaceholder = function () {
  placeholderText.value = ''
  isFocused.value = true
}

const restorePlaceholder = function () {
  placeholderText.value = 'MOVIE NOMAD'
  isFocused.value = false
}

const qnas = ref([
  { question: '단축키 모드는 무엇인가요?', answer: '단축키 모드는 마우스를 사용하지 않고도 사이트를 조작할 수 있는 편리한 모드입니다. 안내 팝업창을 확인해주세요!', open: false },
  { question: '서비스 사용료가 있나요?', answer: '해당 서비스는 무료로 제공되고 있습니다. 우측 하단에 커피 버튼을 누르시면 저희가 커피를 한 잔 할 수 있습니다 :)', open: false },
  { question: '어떤 기기에서 사용할 수 있나요', answer: '저희 서비스는 모바일과 인터넷 모두에서 사용 가능합니다.', open: false },
  { question: 'Team M.A.D에 대해 알려주세요.', answer: 'M.A.D는 Making A Difference의 약자로, 저희는 작은 변화로 사회에 기여하고자 합니다.', open: false }
])

const toggle = index => {
  qnas.value[index].open = !qnas.value[index].open
}

</script>

<style scoped>
.main-background {
  width: 100%;
  height: 85vh;
  opacity: 0.85;
  object-fit: cover;
}

.custom-top {
  top: 30vh !important;
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
  box-shadow: 0 4px 6px 0 hsla(0, 0%, 0%, 0.2);
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
  padding: 10px 20px;
  border: 0;
  border-radius: 30px;
  background-color: rgb(32, 32, 32);
  color: white;
  width: 400px;
}

.posterBox {
  height: 500px;
}

.qnaBox {
  height: 500px;
  background-color: #92DE4A;
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
}</style>
