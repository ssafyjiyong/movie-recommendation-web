<template>
  <div>
    <h1>SignupView</h1>

    <form class="signup-form" @submit.prevent="signup">
      <div>
        <label for="username">E-Mail : </label>
        <input v-model="username" type="text" id="username">
      </div>
      <div>
        <label for="nickname">NickName : </label>
        <input v-model="nickname" type="text" id="nickname">
      </div>
      <div>
        <label for="password1">Password : </label>
        <input v-model="password1" type="text" id="password1">
      </div>
      <div>
        <label for="password2">Password Check : </label>
        <input v-model="password2" type="text" id="password2">
      </div>
      <div v-show="passwordCheck">
        비밀번호가 일치하지 않습니다.
      </div>
      <input type="submit" value="signup">
    </form>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useUserStore } from '@/stores/user';

const store = useUserStore()
const username = ref('')
const nickname = ref('')
const password1 = ref('')
const password2 = ref('')

const signup = (payload) => {
  payload = {
    'username': username.value,
    'nickname': nickname.value,
    'password1': password1.value,
    'password2': password2.value,
  }

  store.signUp(payload)
}

const passwordCheck = computed(() => {
  if (password1.value == password2.value || password2.value == '') {
    return false
  } else {
    return true
  }
})
</script>

<style scoped>
.signup-form {
  display: flex;
  flex-direction: column;
}

.signup-form input {
  width: 30%;
}
</style>