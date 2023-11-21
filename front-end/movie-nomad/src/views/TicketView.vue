<template>
  <div>
    <h1>TicketView</h1>
  </div>


  <button @click="goToAddArticle">글쓰기</button>

</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()


const goToAddArticle = function () {
  router.push('/create/3/')
}

</script>

<style scoped>

</style>