import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getMoviesList, getPopularMovies, getUpcomingMovies, getNowPlayingMovies } from '@/apis/movieApi'

export const useMovieStore = defineStore('movie', () => {
  // 전체 영화 정보 저장목록
  const allMovies = ref([])

  // 캐러셀용 이미지 저장목록
  const popularMovieImages = ref([])
  const upcomingMovieImages = ref([])
  const nowPlayingMovieImages = ref([])

  const searchedMovies = ref(allMovies)

  const searchTheMovie = (movieKeyword) => {
    searchMovie(movieKeyword)
    .then((response) => {
        console.log(response.data)
        searchedMovies.value = response.data
      })
      .catch((error) => {
        console.error('Error search the movie', error)
      })
  }

  // 모든 영화 정보
  const initializeMovies = () => {
    getMoviesList()
      .then((response) => {
        if (response && response.data) {
          allMovies.value = response.data
          console.log('모든 영화를 불러왔습니다ㅎㅎ')
        }
      })
      .catch((error) => {
        console.error('Error getting all movies:', error)
      })
  }


  // HomeView캐러셀용 이미지 불러오기
  const getCarouselImages = () => {
    getPopularMovies()
      .then((response) => {
        if (response && response.data) {
          response.data['results'].forEach(movie => {
            popularMovieImages.value.push(movie['poster_path'])
          });
        }

        return popularMovieImages.value
      })
      .then((res) => {
        console.log(res)
      })
  }
  return { allMovies, popularMovieImages, upcomingMovieImages, nowPlayingMovieImages, initializeMovies, getCarouselImages }
})
