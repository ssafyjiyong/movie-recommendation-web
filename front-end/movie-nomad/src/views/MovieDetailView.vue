<template>
  <div class="container topBox" v-if="!loading">
    <!-- Detail의 상단 부분 -->
    <div class="row">
      <!-- Poster -->
      <div class="radiusBox col-3 p-1">
        <img :src="imageFromStore" alt="movie_poster" class="posterImage">

        <div class="d-flex flex-column">
          <small>개봉일: {{ currentMovie.release_date }}</small>
          <small>러닝타임 : {{ currentMovie.runtime }}분</small>
          <small>장르: <div v-for="genre in genres">{{ genre.name }}</div></small>
          <small>평점: {{ currentMovie.vote_average }}</small>
          <small>({{ currentMovie.vote_count }}개의 평가)</small>
          <small>인지도: {{ currentMovie.popularity }}</small>
          <small>감독: <span v-for="director in directors">{{ director.name }}</span></small>
        </div>
      </div>

      <!-- 좋아요 및 영화 내용 -->
      <div class="col-9">
        <!-- 좋아요 및 컬렉션 추가 버튼 등 -->
        <div class="radiusBox d-flex justify-content-around">
          <button class="btn btn-link text-black p-1" @click="likeMovie"><i
              class="fa-regular fa-thumbs-up"></i>좋아요</button>
          <button class="btn btn-link text-black p-1" @click="sosoMovie"><i
              class="fa-solid fa-face-meh"></i>그저그래요</button>
          <button class="btn btn-link text-black p-1" @click="hateMovie"><i
              class="fa-regular fa-thumbs-down"></i>별로예요</button>
          <!-- 컬렉션 모달 띄우기 -->
          <button class="btn btn-link text-black p-1" data-bs-toggle="modal" data-bs-target="#collection">
            <i class="fa-regular fa-bookmark"></i>
            저장
          </button>
          <MovieCollectionModal :moviePk="moviePk" />
          <button class="btn btn-link text-black p-1"><i class="fa-regular fa-pen-to-square"></i>게시글작성</button>
        </div>

        <!-- 영화 내용  -->
        <div class="contentBox">
          <p>{{ currentMovie.overview }}</p>
        </div>
      </div>
    </div>

    <!-- 관련 OST 정보 -->
    <div class="radiusBox d-flex justify-content-between align-items-center">
      <h3>이 영화와 관련된 OST를 들어보실래요?</h3>
      <div>
        <img class="album-jacket" :src="album['image']" alt="">
      </div>
      <button class="btn btn-link text-black" @click="spotify"><i
          class="fa-solid fa-headphones-simple fa-2x"></i></button>
    </div>

    <!-- 감독 및 배우 정보 -->
    <div class="radiusBox">
      <h3>출연진</h3>
      <div class="actors">
        <MovieCredit v-for="actor in actors" :key="actor.id" :actor="actor" />
      </div>
    </div>

    <!-- 컬렉션 정보 -->
    <div class="radiusBox">
      <h3>이 영화를 좋아하는 메이트</h3>
      <MovieMate v-for="mate in movieMates" :key="mate.id" :mate="mate" />
    </div>

    <!-- 게시글 정보 -->
    <div class="radiusBox">
      <h3>관련게시글</h3>
      <hr>
      <CommunityGridCard v-for="article in articles" :key="article.id" :article="article">
        {{ article.title }}
      </CommunityGridCard>
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
import MovieCredit from '@/components/movie/MovieCredit.vue'
import MovieMate from '@/components/movie/MovieMate.vue'
import MovieCollectionModal from '../components/movie/MovieCollectionModal.vue';
import CommunityGridCard from '@/components/community/CommunityGridCard.vue'
import { ref, onMounted } from 'vue';
import { getMovieDetail, getActorsList, getDirectorsList, getGenresList, thisMovieArticles, thisMovieMate, thisMovieOST, likeMovieApi, sosoMovieApi, hateMovieApi } from '@/apis/movieApi'
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movieStore';

defineProps({
  isDarkMode:Boolean,
})

const movieStore = useMovieStore()
const randomMessage = movieStore.loadingMessage[Math.floor(Math.random() * movieStore.loadingMessage.length)];

const route = useRoute()
const currentMovie = ref([])
const moviePk = route.params.movieId

const actors = ref([])
const directors = ref([])
const genres = ref([])
const articles = ref([])
const movieMates = ref([])
const album = ref([])

const loading = ref(true)

const imageFromStore = ref('')

const spotify = () => {
  window.open(album.value['url'])
}

const initializecurrentMovie = (moviePk) => {
  getMovieDetail(moviePk)
    .then((response) => {
      if (response && response.data) {
        currentMovie.value = response.data
        getActorsList(moviePk)
          .then(response => {
            actors.value = response.data.splice(0, 5)
          })
        getDirectorsList(moviePk)
          .then((response) => {
            directors.value = response.data
          })
        getGenresList(moviePk)
          .then((response) => {
            genres.value = response.data
          })
        thisMovieArticles(moviePk)
          .then((response) => {
            // console.log(response.data)
            articles.value = response.data
          })
        thisMovieMate(moviePk)
          .then((response) => {
            // console.log(response.data)
            movieMates.value = response.data
          })
        thisMovieOST(moviePk)
          .then((response) => {
            // console.log(response.data)
            album.value = response.data
          })
        imageFromStore.value = `https://image.tmdb.org/t/p/w500/${currentMovie.value.poster_path}`
        loading.value = false
      }
    })
    .catch((error) => {
      console.error('Error initializing movie detail:', error)
    })
}

const likeMovie = () => {
  likeMovieApi(moviePk)
}

const sosoMovie = () => {
  sosoMovieApi(moviePk)
}

const hateMovie = () => {
  hateMovieApi(moviePk)
}

onMounted(() => {
  initializecurrentMovie(moviePk)
});

</script>

<style scoped>
.posterImage {
  width: 100%;
}

.radiusBox {
  border: 1px solid black;
  border-radius: 10px;
  padding: 20px;
  margin: 10px 0px;
}

.contentBox {
  height: auto;
  border: 1px solid black;
  border-radius: 10px;
  padding: 20px;
  margin: 10px 0px;
}

.actors {
  display: flex;
}

.album-jacket {
  width: 30%;
  height: 30%;
}
</style>