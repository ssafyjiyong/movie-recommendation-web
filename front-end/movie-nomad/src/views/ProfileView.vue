<template>
  <router-view :key="route.fullPath" />
  <div class="topContainer d-flex">
    <!-- 프로필 사진 및 상태 -->
    <div class="col-4">
      <!-- 프로필 사진과 이름, 닉네임 -->
      <div class="text-center">
        <div v-show="!profileExist">
          <img src="@/images/main_background.jpg" alt="profile_img" class="profileImage my-2">
        </div>
        <div v-show="profileExist">
          <img :src="`http://localhost:8000${userInfo.profile_pic}`" alt="profile_image" class="profileImage my-2">
        </div>
        <div v-show="isMyProfile">
          <button type="button" data-bs-toggle="modal" data-bs-target="#profilePicture" class="btn btn-link text-secondary p-0">
            <i class="fa-solid fa-camera" style="color: #8eecb2;"></i>
          </button>
          <ProfilePicture />
        </div>
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
        <div class="inBlogBox1 me-4 ps-4">
          <div 
            class="collection-box col-6"
            v-for="collection in collections"
            :key="collection.id"
          >
            <ProfileCollection :collection="collection" />
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
    <button 
      class="btn btn-secondary btn-sm"
      type="button"
      data-bs-toggle="modal"
      data-bs-target="#updatePassword"
    >
      비밀번호 변경
    </button>
    <PasswordUpdate />
    <button v-show="isMyProfile" type="button" data-bs-toggle="modal" data-bs-target="#signOut"
      class="btn btn-danger btn-sm mx-1">회원탈퇴</button>
    <SignOut />
  </div>
</template>


<script setup>
import { following, userProfile, changeStatus } from '../apis/userApi';
import { userArticleList } from '@/apis/movieApi';
import { useUserStore } from '@/stores/userStore';
import { useRoute, useRouter } from 'vue-router';
import { onMounted, ref, computed } from 'vue';

import ProfileArticle from '@/components/profile/ProfileArticle.vue';
import ProfilePicture from '@/components/profile/ProfilePicture.vue';
import ProfileCollection from '@/components/profile/ProfileCollection.vue';
import PasswordUpdate from '@/components/profile/PasswordUpdate.vue';
import SignOut from '@/components/profile/SignOut.vue';


const userStore = useUserStore()
const route = useRoute()
const router = useRouter()

const profileUserNickname = route.params.nickname
const isMyProfile = ref(true)
const updateStatus = ref(false)
const profile_image = ref(true)
const status = ref()
const articles = ref([])
const userInfo = ref([])
const collections = ref([])

const profileExist = computed(() => {
  return profile_image.value
})

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
onMounted(() => {
  userProfile(profileUserNickname)
    .then((response) => {
      console.log(response.data)
      userInfo.value = response.data
      collections.value = response.data.collections
      status.value = userStore.userInfo.status
    })
    .then(() => {
      if (userStore.nickname !== profileUserNickname) {
        isMyProfile.value = false
      }

      if (!userInfo.value.profile_pic) {
        profile_image.value = false
      }
    })
    .catch((error) => {
      console.error('Error initializing userProfile:', error)
      window.alert("유저정보가 존재하지 않습니다.")
      router.push( { name :'home' } )
    })

  userArticleList(route.params.nickname)
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

.inBlogBox1 {
  border: 1px solid black;
  border-radius: 10px;
  padding: 5px;
  display: flex;
  flex-wrap: wrap;
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


.collectionBox {
  display: flex;
}
@media (max-width: 635px) {
  .profileImage {
    display: none;
  }
}
</style>