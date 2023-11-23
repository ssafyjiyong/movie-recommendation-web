<template>
  <li class="list-group-item">
    <div class="d-flex justify-content-between">
    <span>
      {{ items[0].name }}
    </span>
      <button v-show="!isCollected" 
      class="btn btn-success btn-sm"
      @click="addMovie(items[0].pk, items[1])">추가</button>
      <button v-show="isCollected" 
      class="btn btn-danger btn-sm"
      @click="removeMovie(items[0].pk, items[1])">제거</button>
    </div>
  </li>
</template>

<script setup>
import { defineProps, ref, onMounted } from 'vue';
import { addCollection, getCollection } from '@/apis/movieApi';
import Swal from "sweetalert2";

const isCollected = ref(false)
const props = defineProps({
  items: Array
})

const items = props.items


// console.log(items)
const addMovie = (a, b) => {
  addCollection(a, b)
  Swal.fire({
        title: `${props.items[0].name} 컬렉션에 추가되었습니다.`,
        icon: "success",
        confirmButtonColor: "#3085d6",
        confirmButtonText: "확인"
      })
  isCollected.value = true
}

const removeMovie = (a, b) => {
  addCollection(a, b)
  Swal.fire({
        title: `${props.items[0].name} 컬렉션에서 제거되었습니다.`,
        icon: "success",
        confirmButtonColor: "#FFFFFF",
        confirmButtonText: "확인"
      })
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