<template>
  <div class="modal fade" id="collection" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="collection">My Movie Collections</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <ul>
            <li v-for="collection in myCollection" :key="collection.id">{{ collection.name }}</li>
          </ul>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';
import { userCollection } from '@/apis/movieApi';

const userStore = useUserStore()
const myCollection = ref([])

defineProps({
  moviePk: String
})

onMounted(() => {
  userCollection(userStore.userData['pk'])
  .then((response) => {
    console.log(userStore.nickname)
    response.data.forEach(collection => {
      if (collection['user']['nickname'] === userStore.nickname) {
        console.log(response.data)
        myCollection.value.push(collection)
      }
    });
  })
})
</script>

<style scoped>
.modal-content {
  background-color: white;
  opacity: 0.9;
}
</style>