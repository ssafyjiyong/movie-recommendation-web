import { ref } from 'vue'
import { defineStore } from 'pinia'
import {
  getArticlesList,
  createArticleAPI,
  deleteArticleAPI,
  updateArticleAPI
} from '@/apis/movieApi'
import Swal from "sweetalert2";
import router from '../router';

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])

  // 게시글 들어가면 나오는 모든 게시글
  const initializeArticles = () => {
    getArticlesList()
      .then((response) => {
        articles.value = response.data
      })
      .catch((error) => {
        console.error('Error initializing articles:', error)
      })
  }

  // 게시글 생성
  const createArticle = (payload) => {
    return createArticleAPI(payload)
      .then((response) => {
        Swal.fire({
          title: "글 작성 완료!",
          icon: "success",
          confirmButtonColor: "#682cd48c",
          confirmButtonText: "확인",
        });
        articles.value.push(response.data);
        router.push(`/community/${response.data.category}`)
      })
      .catch((error) => {
        console.error(error)
        throw error
      })
  }

  // 게시글 삭제
  const deleteArticle = (articlePk) => {
    return deleteArticleAPI(articlePk)
      .then((response) => {
        if (response) {
          // articles 배열에서 삭제된 게시글을 찾아서 삭제
          const index = articles.value.findIndex((article) => article.pk === articlePk)
          if (index !== -1) {
            articles.value.splice(index, 1)
          }
          return response
        } else {
          window.alert('서버 오류')
        }
      })
      .catch((error) => {
        console.error(error)
        throw error
      })
  }

  // 게시글 업데이트
  const updateArticle = (articlePk, payload) => {
    return updateArticleAPI(articlePk, payload)
      .then((response) => {
        if (response) {
          const article = articles.value.find((article) => article.pk === articlePk)
          if (article) {
            article.content = newContent
          }
          return response
        } else {
          window.alert('서버 오류')
        }
      })
      .catch((error) => {
        console.error(error)
      })
  }

  return {
    articles,
    initializeArticles,
    createArticle,
    deleteArticle,
    updateArticle
  }
})
