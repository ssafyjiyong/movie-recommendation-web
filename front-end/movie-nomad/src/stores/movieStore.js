import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getMoviesList } from '@/apis/movieApi'

export const useMovieStore = defineStore('movie', () => {
  const allMovies = ref([])

  // 모든 영화 정보
  const initializeMovies = () => {
    getMoviesList()
      .then((response) => {
        if (response && response.data) {
          allMovies.value = response.data
        }
      })
      .catch((error) => {
        console.error('Error getting all movies:', error)
      })
  }

  return { allMovies, initializeMovies }
})
