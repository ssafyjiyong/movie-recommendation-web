import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { getMoviesList, searchMovie } from '@/apis/movieApi'

export const useMovieStore = defineStore('movie', () => {
  // 전체 영화 정보 저장목록
  const allMovies = ref([])

  // 캐러셀용 이미지 저장목록
  const popularMovieImages = ref([])
  const upcomingMovieImages = ref([])
  const nowPlayingMovieImages = ref([])

  const searchKeyword = ref('')

  const searchedMovies = computed(() => {
    if (searchKeyword.value) {
      // 검색 키워드가 있을 경우 필터링
      return allMovies.value.filter(movie => movie.title.includes(searchKeyword.value))
    } else {
      // 검색 키워드가 없을 경우 전체 목록 반환
      return allMovies.value
    }
  })

  const searchTheMovie = (movieKeyword) => {
    searchKeyword.value = movieKeyword
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

  return { allMovies, searchedMovies, initializeMovies, searchTheMovie }
})
