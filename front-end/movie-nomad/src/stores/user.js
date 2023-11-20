// userStore.js
import { defineStore } from 'pinia';
import axios from 'axios';
import { ref, computed } from 'vue';

export const useUserStore = defineStore('user', () => {
  const DJANGO_URL = 'http://127.0.0.1:8000/accounts';
  const token = ref(null)
  const username = ref(null)
  const userId = ref(null)
  const nickname = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const signUp = function (payload) {
    axios
      .post(`${DJANGO_URL}/signup/`, payload)
      .then((response) => {
        console.log(response)
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const logIn = function (payload) {
    axios
      .post(`${DJANGO_URL}/login/`, payload)
      .then((response) => {
        token.value = response.data.key
        username.value = payload.username
        return payload.username
      })
      .then((response) => {
        axios
          .get(`http://127.0.0.1:8000/myblog/${response}/`)
          .then((res) => {
            userId.value = res.data.id
            nickname.value = res.data.nickname
            console.log(res.data)
          })
      })
    }

  return { signUp, logIn, token, username, userId, isLogin, nickname }
}, { persist: true })