<template>
  <router-view :key="route.fullPath" />
  <div class="topContainer d-flex">
    <!-- 프로필 사진 및 상태 -->
    <div class="col-4">
      <!-- 프로필 사진과 이름, 닉네임 -->
      <div class="text-center">
        <img src="@/images/main_background.jpg" alt="profile_img" class="profileImage my-2">
        <div class="d-flex justify-content-center align-items-center">
          <span class="fw-bold">{{ profileUserNickname }}</span>의 Blog
          <div v-show="!isMyProfile">
            <button class="btn btn-success btn-sm mx-2" @click="follow">팔로우</button>
          </div>
        </div>
      </div>

      <!-- 팔로우 현황(완료) -->
      <div class="followBox p-2">
        <small class="m-0"><i class="fa-solid fa-users"></i> {{ userInfo.follower_count }} followers · </small>
        <small class="m-0">{{ userInfo.following_count }} followings</small>
      </div>

      <!-- 상태메세지(완료) -->
      <div class="radiusBox">
        <div v-show="!updateStatus">
          <p>{{ userInfo.status }}</p>
          <div v-if="isMyProfile">
                      <div class="d-flex justify-content-end">
              <button @click="statusUpdate" class="btn btn-link text-secondary p-0">
                <i class="fa-regular fa-pen-to-square"></i>
              </button>
            </div>
          </div>
        </div>
        <div v-show="updateStatus">
          <form @submit.prevent="submitStauts">
            <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" style="resize: none;"
              v-model="status"></textarea>
            <input class="btn btn-success btn-sm" type="submit">
          </form>
          <button @click="cancleStatus" class="btn btn-danger btn-sm">취소</button>
        </div>
      </div>

      <!-- 총 영화 본 시간 -->
      <div class="radiusBox text-center">
        <p>와우! <strong>{{ userInfo['total_watch'] }}시간</strong> 보았다 영화를!</p>
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

      <!-- 내가 쓴 게시글(완료) -->
      <div class="articleBox flex-grow-1">
        <ProfileArticle v-for="article in articles" :key="article.id" :article="article" />
      </div>
    </div>
  </div>

  <!-- 회원정보 변경 및 탈퇴 기능 -->
  <div class="d-flex m-2 justify-content-end">
    <RouterLink v-show="isMyProfile" :to="{ name: 'profileUpdate' }">
      <button class="btn btn-secondary btn-sm">회원정보 변경</button>
    </RouterLink>
    <button v-show="isMyProfile" class="btn btn-danger btn-sm mx-1">회원탈퇴</button>
  </div>
</template>

<script setup>
import { following, userProfile, changeStatus } from '../apis/userApi';
import { userArticleList } from '@/apis/movieApi';
import { useUserStore } from '@/stores/userStore';
import { useRoute } from 'vue-router';
import { onMounted, ref, computed } from 'vue';

import ProfileArticle from '@/components/profile/ProfileArticle.vue';


const userStore = useUserStore()
const route = useRoute()

const profileUserNickname = route.params.nickname
const isMyProfile = ref(true)
const updateStatus = ref(false)
const status = ref()
const articles = ref([])
const userInfo = ref([])

// 팔로우
const follow = () => {
  const payload = {
    'token': userStore.token,
    'nickname': route.params.nickname
  }
  following(payload)
  location.reload()
}

// 상태 변경
const statusUpdate = () => {
  updateStatus.value = true
}

const submitStauts = () => {
  const payload = {
    status: status.value
  }
  changeStatus(payload, userStore.userData['pk'])
    .then(() => {
      window.alert("변경되었습니다.")
      updateStatus.value = false
      userStore.userInfo.status = status.value
      location.reload()
    })
}

const cancleStatus = () => {
  status.value = userStore.userInfo.status
  updateStatus.value = false
}

// 다크모드?
defineProps({
  isDarkMode: Boolean,
})

// 프로필 유저정보 불러오기
onMounted(async() => {
  await userProfile(profileUserNickname)
    .then((response) => {
      userInfo.value = response.data
      status.value = userStore.userInfo.status
    })
    .then(() => {
      if (userInfo.value.nickname !== profileUserNickname) {
        isMyProfile.value = false
      }
    })
    .catch((error) => {
      console.error('Error initializing userProfile:', error)
    })

  await userArticleList(route.params.nickname)
    .then((response) => {
      articles.value = response.data
    })
    .catch((error) => {
      console.log("서버가 아파요...")
    })
})
/////////////////////////////////////////////////////////////////




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