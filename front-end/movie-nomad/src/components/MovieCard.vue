<template>
  <div class="cardBox">
    <div class="cardInnerBox d-flex">
      <!-- 그림 -->
      <div class="flex-grow-1 text-center">
        <img @click="goToDetail(searchedMovie.pk)" :src="getMoviePosterUrl(searchedMovie.poster_path)" alt="movie_poster"
          class="posterImage cursorEffect">
      </div>


      <!-- 상세정보 -->
      <div class="col-12 col-sm-9 col-lg-10 d-flex">

        <!-- 제목 및 내용 -->
        <div class="col-12 col-md-9">
          <!-- 영화제목 -->
          <div class="cursorEffect" @click="goToDetail(searchedMovie.pk)">
            <small class="fw-bold">{{ searchedMovie.title }}</small>
          </div>
          <hr class="my-2">
          <!-- 영화내용 -->
          <div class="overview">
            <small v-if="movieContent" v-html="movieContent"></small>

            <div v-else>
              <small>영화 내용을 찾는 중입니다</small>
              <i class="mx-1 fa-regular fa-face-sad-tear"></i>
            </div>

          </div>
        </div>

        <!-- 기타정보(장르 등) -->
        <div class="flex-grow-1 ectInfo border-left ps-1">
          <small>개봉일: {{ formatDate(searchedMovie.release_date) }}</small><br>
          <small>평점: {{ formatVoteAverage(searchedMovie.vote_average) }}</small><br>
          <small>평가수: {{ formatVoteCount(searchedMovie.vote_count) }}개</small>
        </div>

      </div>


    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()

const props = defineProps({
  searchedMovie: Object,
})

const movieContent = computed(() => {
  return props.searchedMovie.overview || null;
});

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

const formatDate = (date) => {
  if (date) {
    return date.replace(/-/g, '.');
  }
  return '';
};

const formatVoteAverage = (voteAverage) => {
  if (voteAverage) {
    return (voteAverage / 2).toFixed(1) + '/5.0';
  }
  return '';
};

const formatVoteCount = (voteCount) => {
  if (voteCount) {
    return voteCount.toLocaleString();
  }
  return '';
};


</script>

<style scoped>
.cursorEffect {
  cursor: pointer;
}
.border-left {
  border-left: 1px solid #ccc;
}
.cardBox {
  margin: 5px;
  background-color: white;
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