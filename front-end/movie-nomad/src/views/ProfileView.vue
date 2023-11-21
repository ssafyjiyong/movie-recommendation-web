<template>
  <div class="topContainer d-flex">
    <!-- 프로필 사진 및 상태 -->
    <div class="col-4">
      <!-- 프로필 사진과 이름, 닉네임 -->
      <div class="text-center">
        <img src="@/images/main_background.gif" alt="profile_img" class="profileImage">
        <div class="d-flex justify-content-center">
          <span>{{ userStore.nickname }}</span>
          <button @click="follow">팔로우</button>
        </div>
      </div>

      <!-- 팔로우 현황 -->
      <div class="radiusBox row">
        <div class="col-6">
          <p class="m-0">팔로우 : 0 명</p>
        </div>
        <div class="col-6">
          <p class="m-0">팔로잉 : 0 명</p>
        </div>
      </div>

      <!-- 상태메세지 -->
      <div class="radiusBox">
        <p>{{ userStore.status }}</p>
        <div class="d-flex justify-content-end">
          <button class="btn btn-link text-secondary p-0">
            <i class="fa-regular fa-pen-to-square"></i>
          </button>
        </div>
      </div>

      <!-- 총 영화 본 시간 -->
      <div class="radiusBox text-center">
        <p>와우! <strong>1102시간</strong> 보았다 영화를!</p>
      </div>
    </div>

    <!-- 블로그 형식 -->
    <div class="blogBox col-8 d-flex flex-column">
      <!-- 컬렉션과 내 영화 정보(좋아하는 장르 등) -->
      <div class="d-flex justify-content-between">
        <!-- 컬렉션 -->
        <div class="inBlogBox flex-grow-1 me-2">
          <div class="text-center">
            <small>Collection</small>
          </div>
          <div class="text-center">
            <img 
            src="@/images/image1.jpg" 
            alt="collection_img" 
            class="collectionImage" 
            v-for="index in Array(4).fill()">
          </div>
        </div>

        <!-- 나의 영화 정보 -->
        <div class="inBlogBox col-6">
          <p>좋아하는 영화 들어갈 자리</p>
        </div>
      </div>

      <!-- 내가 쓴 게시글 -->
      <div class="articleBox flex-grow-1">
        <p>게시글 들어갈 자리</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/userStore';
import { onMounted } from 'vue';
import { following } from '../apis/userApi';
import { useRoute } from 'vue-router';

const userStore = useUserStore()
const route = useRoute()

console.log(route.params.nickname)
console.log(userStore.token)


const follow = () => {
  payload = {
    'token': userStore.token,
    'nickname': route.params.nickname
  }
  following(payload)
}
</script>

<style scoped>
.topContainer {
  padding: 20px;
  height: 90vh;
}

.profileImage {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: 50%;
}

.collectionImage {
  width: 35%;
}

.radiusBox {
  border: 1px solid black;
  border-radius: 10px;
  padding: 20px;
  margin: 10px 0px;
}

.inBlogBox {
  border: 1px solid black;
  border-radius: 10px;
  padding: 5px;
}

.blogBox {
  border: 1px solid black;
  border-radius: 10px;
  padding: 20px;
  margin: 10px 10px;
}

.blogBox>* {
  margin: 5px;
}

.articleBox {
  border: 1px solid black;
  border-radius: 10px;
  padding: 5px;
}
</style>