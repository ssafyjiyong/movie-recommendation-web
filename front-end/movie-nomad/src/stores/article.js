import { defineStore } from 'pinia';
import axios from 'axios';
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';

export const useArticleStore = defineStore('article', () => {
  const userStore = useUserStore()
  const token = userStore.token
  const articles = ref([])
  const DJANGO_URL = 'http://127.0.0.1:8000/community';

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${DJANGO_URL}/caht/`,
    })
      .then((res) =>{
        console.log(res.data)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const addArticles = function (payload) {
    const { userid, category, title, movieid, content } = payload

    axios({
      method: 'POST',
      url: `${DJANGO_URL}/caht/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        userid, category, title, movieid, content
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