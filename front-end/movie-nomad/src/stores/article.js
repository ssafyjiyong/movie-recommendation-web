import { defineStore } from 'pinia';
import axios from 'axios';
import { ref } from 'vue';

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const DJANGO_URL = 'http://127.0.0.1:8000/movies';

  const getArticles = function (movieKeyword) {
    axios({
      method: 'get',
      url: `${DJANGO_URL}/caht/`,
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

  const addArticles = function (payload) {
    const { userid, category, title, movieid, content, image } = payload

    axios({
      method: 'POST',
      url: `${DJANGO_URL}/caht/`,
      data: {
        userid, category, title, movieid, content, image
      }
    })
      .then((res) =>{
        console.log(res.data)
        // searchedMovie.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { getArticles, addArticles }
}, { persist: true })