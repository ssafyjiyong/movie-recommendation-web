<template>
  <div class="container mt-3">
    <h1 class="title fw-bold">{{ route.params.nickname }}의 영화컬렉션</h1>
    <hr>
    <CollectionCard
      v-for="collection in collections"
      :key="collection.id"
      :collection="collection"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { userProfile } from '../apis/userApi';
import Swal from "sweetalert2";
import CollectionCard from '@/components/CollectionCard.vue';

const route = useRoute()
const collections = ref([])

onMounted(() => {
  userProfile(route.params.nickname)
    .then((response) => {
      // console.log(response.data)
      collections.value = response.data.collections
    })
    .catch((error) => {
      console.error('Error initializing userProfile:', error)
      Swal.fire({
        title: `유저 정보가 존재하지 않습니다.`,
        icon: "success",
        confirmButtonColor: "#DC3545",
        confirmButtonText: "확인"
      })
      router.push({ name: 'home' })
    })
})
</script>

<style scoped>
.title {
  color: #A4D179;
}
</style>