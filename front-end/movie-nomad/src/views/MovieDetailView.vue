<template>
  <div class="container topBox" v-if="currentMovie">
    <!-- Detail의 상단 부분 -->
    <div class="row">
      <!-- Poster -->
      <div class="radiusBox col-3 p-1">
        <div v-if="!imagloading">
          <img :src="imageFromStore" alt="movie_poster" class="posterImage">
        </div>

        <div v-else>
          <div class="spinner-border" role="status">
            <span class="visually-hidden">Loading...</span>
          </div>
        </div>

        <div class="d-flex flex-column">
          <small>개봉일: {{ currentMovie.release_date }}</small>
          <small>러닝타임 : {{ currentMovie.runtime }}분</small>
          <small>장르: {{ currentMovie.genres }}</small>
          <small>평점: {{ currentMovie.vote_average }}</small>
          <small>({{ currentMovie.vote_count }}개의 평가)</small>
          <small>인지도: {{ currentMovie.popularity }}</small>
          <small>감독: {{ currentMovie.director }}</small>
        </div>
      </div>

      <!-- 좋아요 및 영화 내용 -->
      <div class="col-9">
        <!-- 좋아요 및 컬렉션 추가 버튼 등 -->
        <div class="radiusBox d-flex justify-content-around">
          <button class="btn btn-link text-black p-1" @click="likeMovie"><i class="fa-regular fa-thumbs-up"></i>좋아요</button>
          <button class="btn btn-link text-black p-1" @click="sosoMovie"><i class="fa-solid fa-face-meh"></i>그저그래요</button>
          <button class="btn btn-link text-black p-1" @click="hateMovie"><i class="fa-regular fa-thumbs-down"></i>별로예요</button>
          <button class="btn btn-link text-black p-1"><i class="fa-regular fa-bookmark"></i>저장</button>
          <button class="btn btn-link text-black p-1"><i class="fa-regular fa-pen-to-square"></i>게시글작성</button>
        </div>
        <!-- 영화 내용  -->
        <div class="radiusBox">
          <p>{{ currentMovie.overview }}</p>
        </div>
      </div>
    </div>

    <!-- 관련 OST 정보 -->
    <div class="radiusBox d-flex justify-content-between align-items-center">
      <h3>이 영화와 관련된 OST를 들어보실래요?</h3>
      <button class="btn btn-link text-black"><i class="fa-solid fa-headphones-simple fa-2x"></i></button>
    </div>

    <!-- 감독 및 배우 정보 -->
    <div class="radiusBox">
      <h3>출연진</h3>
      <div class="actors">
        <MovieCredit 
          v-for="actor in actors"
          :key="actor.id"
          :actor="actor"
        />
      </div>
    </div>

    <!-- 컬렉션 정보 -->
    <div class="radiusBox">
      <h3>팔로워 중에 이 영화를 좋아하는 친구가 있어요!(있을 경우 랜더링)</h3>
    </div>

    <!-- 게시글 정보 -->
    <div class="radiusBox">
      <h3>관련게시글</h3>
    </div>

  </div>
</template>

<script setup>
import MovieCredit from '@/components/movie/MovieCredit.vue'
import { ref, onMounted } from 'vue';
import { getMovieDetail, getActorsList, likeMovieApi, sosoMovieApi, hateMovieApi } from '@/apis/movieApi'
import { useRoute } from 'vue-router';

const route = useRoute()
const currentMovie = ref([])
const moviePk = route.params.movieId

const imagloading = ref(true)
const imageFromStore = ref('')

const initializecurrentMovie = (moviePk) => {
  getMovieDetail(moviePk)
  .then((response) => {
    if (response && response.data) {
      currentMovie.value = response.data
      imageFromStore.value = `https://image.tmdb.org/t/p/w500/${currentMovie.value.poster_path}`
      imagloading.value = false
      }
    })
    .catch((error) => {
      console.error('Error initializing movie detail:', error)
    })
}

const actors = ref([])

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
  getActorsList(moviePk)
  .then(response => {
    actors.value = response.data.splice(0, 5)
  })
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

.actors {
  display: flex;
}
</style>