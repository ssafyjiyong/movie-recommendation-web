<template>
  <div class="list">
    <li>{{ items[0].name }}</li>
    <button @click="addMovie(items[0].pk, items[1])">+</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { addCollection } from '@/apis/movieApi';

defineProps({
  items: Array
})

// console.log(items)
const addMovie = (a, b) => {
  addCollection(a, b)
}
</script>

<style scoped>
.list {
  display: flex;
  justify-content: space-between;
}
</style>