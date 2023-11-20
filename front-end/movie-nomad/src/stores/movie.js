// movieStore.js
import { defineStore } from 'pinia';
import axios from 'axios';
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';


export const useMovieStore = defineStore('movie', () => {
  const userStore = useUserStore()
  const searchedMovie = ref([])
  const token = userStore.token
  const DJANGO_URL = 'http://127.0.0.1:8000/movies';

  // DRF에 movies 조회 요청을 보내는 action
  const searchMovie = function (movieKeyword) {
    axios({
      method: 'get',
      url: `${DJANGO_URL}/movie_search/${movieKeyword}`,
    })
      .then((res) =>{
        console.log(res.data)
        // searchedMovie.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getMovies = function () {
    axios({
      method: 'get',
      url: `${DJANGO_URL}/`,
    })
      .then((res) =>{
        console.log(res.data)

      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { searchMovie, getMovies }
}, { persist: true })