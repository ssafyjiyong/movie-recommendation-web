<template>
  <div>

    <!-- 프로필사진, 작성자, 팔로우 -->
    <div class="mx-5 my-1">
      <span class="fw-bold">{{ commentUser }}</span> | 
      <button class="btn btn-primary btn-sm" @click="goProfile">프로필</button>
    </div>

    <div class="mx-4 p-2 bg-light commentBox">

    <div>
      <p class="m-0 p-2">{{ comment.content }}</p>
    </div>
    <div class="d-flex justify-content-between align-items-start">
        <div>
          <button class="btn btn-light btn-sm border mx-1">답글</button>
        </div>
  
        <div>
          <button @click="likeComment" class="btn btn-outline-danger m-2 border-danger"><i class="fa-regular fa-thumbs-up"></i>{{ comment.like_user_count }}</button>
        </div>
      </div>
  </div>
  

  </div>
  <hr>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { getCommentAPI, likeCommentAPI } from '../../apis/movieApi';
import { useUserStore } from '@/stores/userStore';

const userStore = useUserStore()
const router = useRouter()
const comment = ref([])
const commentUser = ref('')

const likeComment = () => {
  likeCommentAPI(userStore.userData.pk)
    .then((response) => {
      comment.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
}

const goProfile = () => {
  router.push(`/profile/${commentUser.value}`)
}

const props = defineProps({
  comment: Object
})

onMounted(() => {
  getCommentAPI(props.comment.pk)
  .then((response) => {
    console.log(response.data)
    comment.value = response.data
    commentUser.value = response.data.user.nickname
  })
})
</script>

<style scoped>
.commentBox {
  border-radius: 20px;
  width: 60%;
}
.btn-follow {
  background-color: #CFE2FF;
  color: #0D6EFD;
}
.btn-follow:hover {
  background-color: #0D6EFD;
  color: white;
}
</style>