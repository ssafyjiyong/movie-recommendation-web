<template>
  <div class="container topBox" v-if="movieDetail">
    <!-- Detail의 상단 부분 -->
    <div class="row">
      <!-- Poster -->
      <div class="radiusBox col-3">
        <img 
        :src="`https://image.tmdb.org/t/p/w500/${movieDetail.poster_path}`" 
        alt="movie_poster" 
        class="posterImage">
      </div>

      <!-- 좋아요 및 영화 내용 -->
      <div class="col-9">
        <!-- 좋아요 및 컬렉션 추가 버튼 등 -->
        <div class="radiusBox">

        </div>
        <!-- 영화 내용 및 앨범 -->
        <div class="radiusBox">

        </div>
      </div>
    </div>

    <!-- 감독 및 배우 정보 -->
    <div class="radiusBox">

    </div>

    <!-- 컬렉션 정보 -->
    <div class="radiusBox">

    </div>

    <!-- 게시글 정보 -->
    <div class="radiusBox">

    </div>

    {{ movieDetail }}

  </div>
</template>

<script setup>
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';

const route = useRoute()
const router = useRouter()
const movieDetail = ref(null)

const movieId = route.params.movieId

const getMovieDetail = function () {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/movies/movie_detail/${movieId}/`,
  })
    .then((res) => {
      console.log(res.data)
      movieDetail.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
}

onMounted(() => {
  getMovieDetail()
});

</script>

<style scoped>
.radiusBox {
  border: 1px solid black;
  border-radius: 10px;
  padding: 20px;
  margin: 10px 0px;
}
</style>