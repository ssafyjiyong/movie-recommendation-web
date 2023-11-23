<template>
  <div class="modal fade text-black" id="collection" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5 fw-bold" id="collection">나의 컬렉션</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>

        </div>
        <div class="modal-body">
          <ul class="list-group list-group-flush">
            <MovieCollectionModalList v-for="collection in myCollection" :key="collection.id"
              :items="[collection, moviePk]" />
          </ul>
        </div>
        <div v-show="toggle" class="modal-footer">
          <input type="text" placeholder="Collection Name" v-model="collectionName">
          <button @click="makeCollection" class="btn btn-outline-success btn-sm">만들기</button>
          <button @click="newCollectionCancle" class="btn btn-outline-danger btn-sm">취소</button>
        </div>
        <div v-show="!toggle" class="modal-footer">
          <button @click="newCollection" type="button" class="btn btn-primary btn-sm">새로운 컬렉션</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';
import { userCollection, createCollection } from '@/apis/movieApi';
import MovieCollectionModalList from '@/components/movie/MovieCollectionModalList.vue'
import Swal from "sweetalert2";

const userStore = useUserStore()
const myCollection = ref([])
const toggle = ref(false)
const deleteToggle = ref(false)

const collectionName = ref('')
const newCollection = () => {
  toggle.value = true
}
const newCollectionCancle = () => {
  toggle.value = false
}

const makeCollection = () => {
  createCollection(collectionName.value)
    .then((response) => {
      Swal.fire({
        title: `컬렉션이 성공적으로 생성되었습니다.`,
        icon: "success",
        confirmButtonColor: "#3085d6",
        confirmButtonText: "확인"
      })
      toggle.value = false
    })
    .then(() => {
      myCollection.value = []
    })
    .then(() => {
      userCollection(userStore.userData['pk'])
        .then((response) => {
          // console.log(userStore.nickname)
          response.data.forEach(collection => {
            if (collection['user']['nickname'] === userStore.nickname) {
              // console.log(response.data)
              myCollection.value.push(collection)
            }
          });
        })
    })
    .catch((error) => {
      console.log("서..버에...러")
    })
}

defineProps({
  moviePk: String
})

onMounted(() => {
  userCollection(userStore.userData['pk'])
    .then((response) => {
      // console.log(userStore.nickname)
      response.data.forEach(collection => {
        if (collection['user']['nickname'] === userStore.nickname) {
          // console.log(response.data)
          myCollection.value.push(collection)
        }
      });
    })
})
</script>

<style scoped>
.modal-content {
  background-color: white;
}
</style>