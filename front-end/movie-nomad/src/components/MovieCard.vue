<template>
  <div class="cardBox">
    <div class="cardInnerBox d-flex">
      <!-- 그림 -->
      <div class="flex-grow-1 text-center">
        <img :src="getMoviePosterUrl(searchedMovie.poster_path)" alt="movie_poster" class="posterImage">
      </div>


      <!-- 상세정보 -->
      <div class="col-12 col-sm-9 col-lg-10 d-flex">

        <!-- 제목 및 내용 -->
        <div class="col-9">
          <!-- 영화제목 -->
          <div>
            <small class="fw-bold">{{ searchedMovie.title }}</small>
          </div>
          <hr class="my-2">
          <!-- 영화내용 -->
          <div class="overview">
            <small>{{ searchedMovie.overview }}</small>
          </div>
        </div>

        <!-- 기타정보(장르 등) -->
        <div class="col-3">
          <small>개봉일 : {{ searchedMovie.release_date }}</small><br>
          <small>인지도 점수 : {{ searchedMovie.popularity }}</small><br>
          <small>평점 : {{ searchedMovie.vote_average }}</small>
        </div>
      </div>


    </div>
  </div>
</template>

<script setup>
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
</style>