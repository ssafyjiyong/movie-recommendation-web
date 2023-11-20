<template>
  <div class="container topBox">
    <!-- Detail의 상단 부분 -->
    <div class="row">
      <!-- Poster -->
      <div class="radiusBox col-3">
        <img
        :src="getMoviePosterUrl(movieStore.movieDetail.poster_path)" 
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

  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import { onMounted, watch } from 'vue';

const route = useRoute()
const router = useRouter()
const movieStore = useMovieStore()

const movieId = route.params.movieId

const getMoviePosterUrl = (posterPath) => {
  if (posterPath) {
    const baseUrl = 'https://image.tmdb.org/t/p/w500';
    return `${baseUrl}${posterPath}`;
  } else {
    return '';
  }
};

onMounted(async () => {
  await movieStore.getMovieDetail(movieId);
});

watch(() => movieStore.movieDetail, (newValue, oldValue) => {
  console.log(newValue);
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