<template>
  <div class="list">
    <li>{{ items[0].name }}</li>
    <div v-show="!isCollected">
      <button @click="addMovie(items[0].pk, items[1])">+</button>
    </div>
    <div v-show="isCollected">
      <button @click="removeMovie(items[0].pk, items[1])">-</button>
    </div>
  </div>
</template>

<script setup>
import { defineProps, ref, onMounted, computed } from 'vue';
import { addCollection, getCollection } from '@/apis/movieApi';


const isCollected = ref(false)
const props = defineProps({
  items: Array
})

const items = props.items


// console.log(items)
const addMovie = (a, b) => {
  addCollection(a, b)
  window.alert("영화 겟 ☆!")
  isCollected.value = true
}

const removeMovie = (a, b) => {
  addCollection(a, b)
  window.alert("피죤투 꼭 다시 데리러 올게!")
  isCollected.value = false
}

onMounted(() => {
  getCollection(items[0]['pk'])
    .then((response) => {
      response.data.movie.forEach(movie => {
        if (Number(items[1]) === movie) {
          isCollected.value = true
        }
      });
    })
})
</script>

<style scoped>
.list {
  display: flex;
  justify-content: space-between;
}
</style>