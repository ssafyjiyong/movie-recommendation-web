// movieStore.js
import { defineStore } from 'pinia';
import axios from 'axios';
import { ref } from 'vue';

export const useMovieStore = defineStore('movie', () => {
  const searchedMovie = ref([])
  const DJANGO_URL = 'http://127.0.0.1:8000/movies';

  // DRF에 movies 조회 요청을 보내는 action
  const searchMovie = function (movieKeyword) {
    axios({
      method: 'get',
      url: `${DJANGO_URL}/movie_search/${movieKeyword}`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        console.log(res.data)
        // searchedMovie.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { DJANGO_URL, searchMovie }
}, { persist: true })