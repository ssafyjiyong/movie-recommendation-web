// movieStore.js
import { defineStore } from 'pinia';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router'


export const useMovieStore = defineStore('counter', () => {
  const router = useRouter()
  const searchedMovie = ref([])
  const articles = ref([])
  const DJANGO_URL = 'http://127.0.0.1:8000/movies';
  // const token = ref(null)
  // const isLogin = computed(() => {
  //   if (token.value === null) {
  //     return false
  //   } else {
  //     return true
  //   }
  // })

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

  // const signUp = function (payload) {
  //   const { username, password1, password2 } = payload

  //   axios({
  //     method: 'post',
  //     url: `${DJANGO_URL}/accounts/signup/`,
  //     data: {
  //       username, password1, password2
  //     }
  //   })
  //     .then((res) => {
  //       console.log(res)
  //       const password = password1
  //       logIn({ username, password })
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //     })
  // }

  // const logIn = function (payload) {
  //   const { username, password } = payload

  //   axios({
  //     method: 'post',
  //     url: `${DJANGO_URL}/accounts/login/`,
  //     data: {
  //       username, password
  //     }
  //   })
  //     .then((res) => {
  //       console.log(res.data)
  //       token.value = res.data.key
  //       router.push({ name: 'ArticleView' })
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //     })
  // }

  // const logOut = function () {
  //   axios({
  //     method: 'post',
  //     url: `${DJANGO_URL}/accounts/logout/`,
  //   })
  //     .then((res) => {
  //       token.value = null
  //       router.push({ name: 'ArticleView' })
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //     })
  // }

  return { DJANGO_URL, searchMovie }
}, { persist: true })