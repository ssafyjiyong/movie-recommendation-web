<template>
  <div class="container topBox text-black" v-if="!loading">
    <!-- Detail의 상단 부분 -->
    <div class="row">
      <!-- Poster -->
      <div class="radiusBox col-3 p-1 m-2 mb-0">
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
      <div class="col  d-flex flex-column ps-0">
        <!-- 좋아요 및 컬렉션 추가 버튼 등 -->
        <div class="radiusBox d-flex flex-column">

          <div class="d-flex justify-content-around">
            <span class="p-1" @click="likeMovie">
              <i class="fa-regular fa-thumbs-up"></i>좋아요</span>
            <span class="p-1" @click="sosoMovie">
              <i class="fa-solid fa-face-meh"></i>
              그저그래요</span>
            <span class="p-1" @click="hateMovie">
              <i class="fa-regular fa-thumbs-down"></i>
              별로예요</span>
          </div>


          <!-- 컬렉션 모달 띄우기 -->
          <div class="d-flex justify-content-end">
            <span class="p-1" data-bs-toggle="modal" data-bs-target="#collection">
              <i class="fa-regular fa-bookmark"></i>
              저장
            </span>
            <MovieCollectionModal :moviePk="moviePk" />
            <span class="p-1"><i class="fa-regular fa-pen-to-square"></i>게시글작성</span>
          </div>
        </div>

        <!-- 영화 내용  -->
        <div class="contentBox flex-grow-1 my-0">
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

      <CommunityGridCard 
      v-for="article in allArticles" 
      :key="article.id" :article="article">
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
import { useUserStore } from '@/stores/userStore';

defineProps({
  isDarkMode: Boolean,
})

const userStore = useUserStore()
const movieStore = useMovieStore()
const randomMessage = movieStore.loadingMessage[Math.floor(Math.random() * movieStore.loadingMessage.length)];

const route = useRoute()
const currentMovie = ref([])
const moviePk = route.params.movieId

const actors = ref([])
const directors = ref([])
const genres = ref([])
const allArticles = ref([])
const movieMates = ref([])
const album = ref([])

const loading = ref(true)

const imageFromStore = ref('')

const spotify = () => {
  window.open(album.value['url'])
}

const initializecurrentMovie = async (moviePk) => {
  try {
    const detailResponse = await getMovieDetail(moviePk)
    const actorsResponse = getActorsList(moviePk)
    const directorsResponse = getDirectorsList(moviePk)
    const genresResponse = getGenresList(moviePk)
    const articlesResponse = thisMovieArticles(moviePk)
    const matesResponse = thisMovieMate(moviePk)
    const ostResponse = thisMovieOST(moviePk)

    const [
      actorsData,
      directorsData,
      genresData,
      articlesData,
      matesData,
      ostData
    ] = await Promise.all([
      actorsResponse,
      directorsResponse,
      genresResponse,
      articlesResponse,
      matesResponse,
      ostResponse
    ])

    if (detailResponse && detailResponse.data) {
      currentMovie.value = detailResponse.data
      actors.value = actorsData.data.splice(0, 5)
      directors.value = directorsData.data
      genres.value = genresData.data
      allArticles.value = articlesData.data
      movieMates.value = matesData.data
      album.value = ostData.data
      imageFromStore.value = `https://image.tmdb.org/t/p/w500/${currentMovie.value.poster_path}`
    }
  } catch (error) {
    console.error('Error initializing movie detail:', error)
  } finally {
    loading.value = false
  }
}

const likeMovie = () => {
  likeMovieApi(moviePk, userStore.userInfo.nickname)
}

const sosoMovie = () => {
  sosoMovieApi(moviePk, userStore.userInfo.nickname)
}

const hateMovie = () => {
  hateMovieApi(moviePk, userStore.userInfo.nickname)
}

onMounted(() => {
  initializecurrentMovie(moviePk)
});

</script>

<style scoped>
span {
  cursor: pointer;
}

.topBox {
  background-color: #F6FFE8;
}

.posterImage {
  width: 100%;
}

.radiusBox {
  border: 1px solid black;
  border-radius: 10px;
  padding: 10px;
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