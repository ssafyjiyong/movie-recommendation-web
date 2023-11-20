// userStore.js
import { defineStore } from 'pinia';
import axios from 'axios';
import { ref } from 'vue';

export const useUserStore = defineStore('user', () => {
  const DJANGO_URL = 'http://127.0.0.1:8000/accounts';
  const token = ref(null)
  const username = ref(null)

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
        console.log(token.value)
        console.log(response)
        return payload.username
      })
      .then((response) => {
        console.log(response)
        axios
          .get(`http://127.0.0.1:8000/myblog/${response}/`)
          .then((response) => {
            console.log(response.data)
          })
      })
    }

  return { signUp, logIn }
}, { persist: true })