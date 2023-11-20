<template>
  <div class="cardBox">
    <div class="cardInnerBox d-flex">
      <!-- 그림 -->
      <div class="flex-grow-1 text-center">
        <img
        @click="goToDetail(searchedMovie.pk)" 
        :src="getMoviePosterUrl(searchedMovie.poster_path)" 
        alt="movie_poster" 
        class="posterImage">
      </div>


      <!-- 상세정보 -->
      <div class="col-12 col-sm-9 col-lg-10 d-flex">

        <!-- 제목 및 내용 -->
        <div class="col-12 col-md-9">
          <!-- 영화제목 -->
          <div @click="goToDetail(searchedMovie.pk)" >
            <small class="fw-bold">{{ searchedMovie.title }}</small>
          </div>
          <hr class="my-2">
          <!-- 영화내용 -->
          <div class="overview">
            <small>{{ searchedMovie.overview }}</small>
          </div>
        </div>

        <!-- 기타정보(장르 등) -->
        <div class="flex-grow-1 ectInfo">
          <small>개봉일 : {{ searchedMovie.release_date }}</small><br>
          <small>인지도 점수 : {{ searchedMovie.popularity }}</small><br>
          <small>평점 : {{ searchedMovie.vote_average }}</small>
        </div>
      </div>


    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()

const props = defineProps({
  searchedMovie: Object,
})

const getMoviePosterUrl = (posterPath) => {
  if (posterPath) {
    const baseUrl = 'https://image.tmdb.org/t/p/w500';
    return `${baseUrl}${posterPath}`;
  } else {
    return '';
  }
};

const goToDetail = function (movieId) {
  router.push(`/moviedetail/${movieId}`)
}

</script>

<style scoped>
.cardBox {
  border: 1px solid black;
  margin: 5px;
}

.cardInnerBox {
  border: 0px solid black;
  padding: 5px;
}

.posterImage {
  height: 140px;
  object-fit: cover;
}

.overview {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

@media (max-width: 600px) {
  .posterImage {
    display: none;
  }
}

/* medium size */
@media (max-width: 768px) {
  .ectInfo {
    display: none;
  }
}
</style>