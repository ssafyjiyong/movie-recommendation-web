// movieStore.js
import { defineStore } from 'pinia';
import axios from 'axios';
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';


export const useMovieStore = defineStore('movie', () => {
  const userStore = useUserStore()
  const movieDetail = ref(null)
  const searchedMovies = ref([])
  const allMovies = ref([])
  const token = userStore.token
  const DJANGO_URL = 'http://127.0.0.1:8000/movies';

  const searchMovie = function (movieKeyword) {
    axios({
      method: 'get',
      url: `${DJANGO_URL}/movie_search/${movieKeyword}`,
    })
      .then((res) =>{
        console.log(res.data)
        searchedMovies.value = res.data
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
        allMovies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getMovieDetail = function(movieId) {
    axios({
      method: 'get',
      url: `${DJANGO_URL}/movie_detail/${movieId}/`,
    })
      .then((res) =>{
        movieDetail.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


  return { searchMovie, getMovies, searchedMovies, allMovies, movieDetail, getMovieDetail }

}, { persist: true })