import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getMoviesList } from '@/apis/movieApi'

export const useMovieStore = defineStore('movie', () => {
  const allMovies = ref([])

  // 이쪽에서 검색된 영화 컨트롤 하도록 재설계(Home이랑 Movies List)
  const searchedMovies = ref(allMovies)

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

  return { allMovies, initializeMovies }
})
