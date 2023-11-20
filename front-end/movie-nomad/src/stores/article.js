import { defineStore } from 'pinia';
import axios from 'axios';
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';

export const useArticleStore = defineStore('article', () => {
  const userStore = useUserStore()
  const token = userStore.token
  const articles = ref([])
  const article = ref([])
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

  const articleDetail = function (articleId) {
    axios({
      method: 'get',
      url: `${DJANGO_URL}/article_detail/${articleId}/`
    })
      .then((res) => {
        console.log(res)
        article.value = res.data
        console.log(article.value)
      })
      .catch((err) => {
        window.alert(err)
      })
  }

  const addArticles = function (payload) {
    const { category, title, movie, content } = payload

    axios({
      method: 'POST',
      url: `${DJANGO_URL}/caht/`,
      headers: {
        Authorization: `Token ${token}`
      },
      data: {
        category, title, movie, content
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

  return { getArticles, articleDetail, addArticles, articles, article }
}, { persist: true })