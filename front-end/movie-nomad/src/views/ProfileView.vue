<template>
  <div class="topContainer d-flex">
    <!-- 프로필 사진 및 상태 -->
    <div class="col-4">
      <!-- 프로필 사진과 이름, 닉네임 -->
      <div class="text-center">
        <img src="@/images/main_background.jpg" 
        alt="profile_img" 
        class="profileImage my-2">
        <div class="d-flex justify-content-center align-items-center">
          <span class="fw-bold">{{ profileUserNickname }}</span>의 Blog
          <button class="btn btn-success btn-sm mx-2" @click="follow">팔로우</button>
        </div>
      </div>

      <!-- 팔로우 현황 -->
      <div class="followBox p-2">
          <small class="m-0"><i class="fa-solid fa-users"></i> {{ userInfo.follower_count }} followers · </small>
          <small class="m-0">{{ userInfo.following_count }} followings</small>
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
            <img src="@/images/image1.jpg" alt="collection_img" class="collectionImage" v-for="index in Array(4).fill()">
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
  
  <!-- 회원정보 변경 및 탈퇴 기능 -->
  <div class="d-flex m-2 justify-content-end">
    <button class="btn btn-secondary btn-sm">회원정보 변경</button>
    <button class="btn btn-danger btn-sm mx-1">회원탈퇴</button>
   </div>
</template>

<script setup>
import { useUserStore } from '@/stores/userStore';
import { onMounted, ref } from 'vue';
import { following, userProfile } from '../apis/userApi';
import { useRoute } from 'vue-router';

defineProps({
  isDarkMode:Boolean,
})

const userStore = useUserStore()
const route = useRoute()
const profileUserNickname = route.params.nickname
const userInfo = ref({})

console.log(userStore.userInfo)

const follow = () => {
  const payload = {
    'token': userStore.token,
    'nickname': route.params.nickname
  }
  following(payload)
}

onMounted(() => {
  if (profileUserNickname === userStore.nickname) {
    console.log('나의 블로그입니다')
    userInfo.value = userStore.userInfo
  } else {
    userProfile(profileUserNickname)
  .then((response) => {
      console.log(response.data)
    })
    .catch((error) => {
      console.error('Error initializing userProfile:', error)
    })
  }
})

</script>

<style scoped>
.topContainer {
  padding: 20px;
  height: 100%;
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
.followBox {
  border: 1px solid black;
  border-radius: 10px;
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

@media (max-width: 635px) {
  .profileImage {
    display: none;
  }
}
</style>