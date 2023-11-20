// userStore.js
import { defineStore } from 'pinia';
import axios from 'axios';
import { ref } from 'vue';

export const useUserStore = defineStore('user', () => {
  const DJANGO_URL = 'http://127.0.0.1:8000/accounts';

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

  return { signUp }
}, { persist: true })