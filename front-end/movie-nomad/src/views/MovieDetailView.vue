<template>
  <div v-if="!loading" class="d-flex justify-content-center">
    <div class="filterTitleBoxTop mx-5 text-white p-2 mb-0">
      <p class="fw-bold m-0">{{ currentMovie.title }}</p>
    </div>
  </div>

  <div class="d-flex justify-content-center">
    <div class="topBox mx-5 text-black" v-if="!loading">


      <!-- Detail의 상단 부분 -->
      <div class="row">
        <!-- Poster -->
        <div class="radiusBox col-3 p-1 m-2 mb-0">
          <div class="text-center py-2">
            <img :src="imageFromStore" alt="movie_poster" class="posterImage rounded">
          </div>

          <div class="d-flex flex-column">
            <small>개봉일: {{ formatDate(currentMovie.release_date) }}</small>
            <small>감독: {{ formatDirector(directors) }}</small>
            <small>장르: {{ formatGenre(genres) }}</small>
            <small>러닝타임 : {{ currentMovie.runtime }}분</small>
            <small>평점: {{ currentMovie.vote_average.toFixed(2) }}점</small>
            <small>({{ formatVoteCount(currentMovie.vote_count) }}개의 평가)</small>
          </div>
        </div>

        <!-- 좋아요 및 영화 내용 -->
        <div class="col  d-flex flex-column ps-0">
<!-- 좋아요 및 컬렉션 추가 버튼 등 -->
<div class="radiusBox d-flex flex-column">

<div class="d-flex justify-content-around">
  <span class="text-primary p-1 cursorEffect" @click="likeMovie">
    <i class="fa-regular fa-thumbs-up"></i> 좋아요</span>
  <span class="text-secondary p-1 mb-2 cursorEffect" @click="sosoMovie">
    <i class="fa-solid fa-face-meh"></i>
    그저그래요</span>
  <span class="text-danger p-1 cursorEffect" @click="hateMovie">
    <i class="fa-regular fa-thumbs-down"></i>
    별로예요</span>
</div>

<!-- 컬렉션 모달 띄우기 -->
<div class="d-flex justify-content-around">
  <span class="text-warning p-1 cursorEffect" data-bs-toggle="modal" data-bs-target="#collection">
    <i class="fa-regular fa-bookmark"></i>
    컬렉션 저장
  </span>
  <MovieCollectionModal :moviePk="moviePk" />
  <span class="text-info p-1 cursorEffect"><i class="fa-regular fa-pen-to-square"></i>게시글작성</span>
</div>
</div>


          <!-- 영화 내용  -->
          <div class="contentBox flex-grow-1 my-0">
            <p>{{ currentMovie.overview }}</p>
          </div>
        </div>
      </div>
      
      <!-- 배우 정보 -->
      <div class="radiusBox">
        <h3>출연진</h3>
        <div class="d-flex justify-content-around">
          <MovieCredit v-for="actor in actors" :key="actor.id" :actor="actor" />
        </div>
      </div>

      <!-- 관련 OST 정보 -->
      <div class="radiusBox">
        <div>
          <h3>{{ currentMovie.title }} OST</h3>
        </div>

        <div class="text-center">
          <img class="album-jacket" :src="album['image']" alt="">
          <button class="btn btn-link text-black" @click="spotify"><i
              class="fa-solid fa-headphones-simple fa-2x"></i></button>
        </div>
      </div>


      <!-- 컬렉션 정보 -->
      <div class="radiusBox">
        <h3>{{ currentMovie.title }}를 좋아하는 메이트</h3>
        <MovieMate v-for="mate in movieMates" :key="mate.id" :mate="mate" />
        <div v-if="movieMates.length === 0">
          <hr class="m-0">
          <div id="articleList" class="d-flex text-center justify-content-center flex-column">
            <div class="pt-3"><i class="fa-regular fa-face-surprise"></i> 이 영화를 좋아하는 메이트가 없어요,</div>
            <div class="p-3 pt-2"> 영화를 보고 후기를 나눠보세요!</div>
          </div>
          <hr class="m-0">
        </div>
      </div>

      <!-- 게시글 정보 -->
      <div class="radiusBox">
        <h3>관련게시글</h3>
        <div class="topArticleBox">
          <div class="latest-article">
            <div class="articleBox d-flex text-center justify-content-between">
              <div class="col-1 py-3">글번호</div>
              <div class="col-7 py-3">글제목</div>
              <div class="col-2 py-3">작성자</div>
              <div class="col-2 py-3">작성일</div>
            </div>
            <hr class="m-0">

            <ArticleCardForMovie v-for="article in allArticles" :key="article.id" :article="article">
              {{ article.title }}
            </ArticleCardForMovie>

            <div v-if="allArticles.length === 0">
              <div id="articleList" class="d-flex text-center justify-content-center">
                <div class="articleTitle p-2">커뮤니티에 관련 글을 작성해보세요!</div>
              </div>
              <hr class="m-0">
            </div>

          </div>
        </div>
      </div>

    </div>

    <div v-else class="d-flex justify-content-center align-items-center m-5">
      <div class="spinner-border text-success d-inline" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      <h3 class="m-3">{{ randomMessage }}</h3>
    </div>
  </div>
</template>

<script setup>
import MovieCredit from '@/components/movie/MovieCredit.vue'
import MovieMate from '@/components/movie/MovieMate.vue'
import MovieCollectionModal from '../components/movie/MovieCollectionModal.vue';
import ArticleCardForMovie from '@/components/community/ArticleCardForMovie.vue'
import { ref, onMounted } from 'vue';
import { getMovieDetail, getActorsList, getDirectorsList, getGenresList, thisMovieArticles, thisMovieMate, thisMovieOST, likeMovieApi, sosoMovieApi, hateMovieApi } from '@/apis/movieApi'
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movieStore';
import { useUserStore } from '@/stores/userStore';


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

// 형식 관련
const formatDate = (dateStr) => {
  const date = new Date(dateStr);
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();
  return `${year}년 ${month.toString().padStart(2, '0')}월 ${day.toString().padStart(2, '0')}일`;
}

const genreMap = {
  'Action': '액션',
  'Adventure': '모험',
  'Animation': '애니메이션',
  'Comedy': '코미디',
  'Crime': '범죄',
  'Documentary': '다큐멘터리',
  'Drama': '드라마',
  'Family': '가족',
  'Fantasy': '판타지',
  'History': '역사',
  'Horror': '공포',
  'Music': '음악',
  'Mystery': '미스터리',
  'Romance': '멜로/로맨스',
  'Science Fiction': 'SF',
  'TV Movie': 'TV 영화',
  'Thriller': '스릴러',
  'War': '전쟁',
  'Western': '서부'
}

const formatGenre = (genres) => {
  return genres.map(genre => genreMap[genre.name] || genre.name).join(' / ');
}

const formatDirector = (directors) => {
  return directors.map(director => director.name).join(' / ');
}

const formatVoteCount = (voteCount) => {
  return voteCount.toLocaleString('ko-KR');
}

// 데이터 모두 불러오기
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
.filterTitleBoxTop {
  background-color: #83C442;
  border-top-right-radius: 0.5rem;
  border-top-left-radius: 0.5rem;
  margin-bottom: 5px;
  width: 90%;
  min-width: 518px;
}

.cursorEffect {
  cursor: pointer;
}
.cursorEffect:hover {
  font-weight: bold;
}
.topBox {
  min-width: 518px;
  width: 90%;
  background-color: #F6FFE8;
  padding: 20px;
  border-end-start-radius: 1.5rem;
  border-end-end-radius: 1.5rem;
  margin-bottom: 20px;
}

.posterImage {
  width: 90%;
}

.radiusBox {
  background-color: white;
  border-radius: 10px;
  padding: 10px;
  margin: 10px 0px;
}

.contentBox {
  height: auto;
  background-color: white;
  border-radius: 10px;
  padding: 20px;
  margin: 10px 0px;
}

.album-jacket {
  width: 20vw;
  height: 20vw;
  border-radius: 5px;
  margin-bottom: 2vh;
}
</style>