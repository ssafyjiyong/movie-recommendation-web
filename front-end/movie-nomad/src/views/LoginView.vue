<template>
  <div>
    <h1>LoginView</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">E-Mail : </label>
        <input type="text" id="username" v-model="username">
      </div>
      <div>
        <label for="password">Password : </label>
        <input type="password" id="password" v-model="password">
      </div>
      <input type="submit" value="login">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';

const store = useUserStore()
const username = ref('')
const password = ref('')

const login = () => {
  const payload = {
    'username': username.value,
    'password': password.value,
  }

  store.logIn(payload)
} 
</script>

<style scoped></style>