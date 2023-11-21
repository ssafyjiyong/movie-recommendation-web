import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getMoviesList, searchMovie } from '@/apis/movieApi'

export const useMovieStore = defineStore('movie', () => {
  
  const allMovies = ref([])
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

  return { allMovies, searchedMovies, initializeMovies, searchTheMovie }
})
