import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getCommentList, createCommentAPI, deleteCommentAPI } from '@/apis/movieApi'

export const useCommentStore = defineStore('comment', () => {

  const comments = ref([])

  // 해당 게시글에 있는 댓글 조회
  const initializeComments = (articlePk) => {
    getCommentList(articlePk)
      .then((response) => {
        if (response && response.data) {
          comments.value = response.data
        }
      })
      .catch((error) => {
        console.error('Error initializing comments:', error)
      })
  }

  // 새로운 코멘트 생성
  const createComment = (articlePk, payload) => {
    return createCommentAPI(articlePk, payload)
      .then((response) => {
        if (response.status === 201) {
          comments.value = response.data
        }
      })
      .catch((error) => {
        console.error('Error creating a new comment:', error)
      })
  }

  // 코멘트 삭제
  const deleteComment = (articlePk, commentPk) => {
    return deleteCommentAPI(articlePk, commentPk)
      .then((response) => {
        if (response.status === 200) {
          comments.value = response.data
        }
      })
      .catch((error) => {
        console.error('Error deleting the comment:', error)
      })
  }

  return { comments, initializeComments, createComment, deleteComment }
})
