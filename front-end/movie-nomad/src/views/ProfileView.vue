<template>
  <router-view :key="route.fullPath" />
  <div class="d-flex justify-content-start superTop">
    <div class="topContainer d-flex">
      <!-- 프로필 사진 및 상태 -->
      <div class="col-4 leftSide text-center">
        <!-- 프로필 사진과 이름, 닉네임 -->
        <div class="text-center">
          <div v-show="!profileExist">
            <img src="@/images/main_background.jpg" alt="profile_img" class="profileImage my-2">
          </div>
          <div v-show="profileExist">
            <img :src="`http://localhost:8000${userInfo.profile_pic}`" alt="profile_image" class="profileImage my-2">
          </div>
          <div v-show="isMyProfile">
            <button type="button" data-bs-toggle="modal" data-bs-target="#profilePicture"
              class="btn btn-link text-secondary p-0 smallDiappear">
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
        <div class="followBox p-2 mt-2 mb-3">
          <small class="m-0"><i class="fa-solid fa-users"></i> {{ userInfo.follower_count }} followers · </small>
          <small class="m-0">{{ userInfo.following_count }} followings</small>
        </div>

        <!-- 상태메세지(완료) -->
        <div class="border rounded-3 p-3">
          <div v-show="!updateStatus">
            <p class="m-0">{{ userInfo.status }}</p>
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
        <div class="border rounded-3 p-4 mt-2">
          <p class="m-0">와우! <strong>{{ userInfo['total_watch'] }}시간</strong> 보았다 영화를!</p>
          <hr class="m-2">
          <small>좋아해, 너, 영화?</small>
        </div>
      </div>

      <!-- 블로그 형식 -->
      <div class="d-flex flex-column rounded-4 mx-2 myBlogBox flex-grow-1 p-3 borderCustom text-black">
        <!-- 컬렉션과 내 영화 정보(좋아하는 장르 등) -->
        <div class="d-flex justify-content-around mb-2">
          <!-- 컬렉션 -->
        <div :class="['minimumBox', 'border', 'col-5', 'rounded-3', isDarkMode ? 'bgCustom-dark' : 'bgCustom']">

            <div class="text-center minLimit">
              <div class="p-1">
                <p class="fw-bold">나의 대표 컬렉션</p>
              </div>
              <hr class="m-0">

              <div v-if="collections.length > 0">
                <div v-for="collection in collections.slice(0, 1)" :key="collection.id">
                  <ProfileCollection :collection="collection" />
                  <button class="btn btn-success btn-sm mb-3" @click="moreCollections">컬렉션 더보기</button>
                </div>
              </div>

              <div v-else class="p-1">
                <p class="m-0">컬렉션이 아직 없습니다.</p>
              </div>
            </div>

          </div>

          <!-- 나의 영화 정보 -->
        <div :class="['text-center', 'border', 'col-5', 'rounded-3','minLimit', 'minimumBox', isDarkMode ? 'bgCustom-dark' : 'bgCustom']">
            <div class="p-1">
              <p class="fw-bold">나의 추천 영화</p>
            </div>
            <hr class="m-0">

            <div v-if="likeMovies.length > 0">
              <div class="likemovie-box" v-for="likeMovie in likeMovies" :key="likeMovie.id">
                <div class="d-flex justify-content-center">
                  <div class="border w-75 rounded-3 my-1 minLimit">
                    <p class="m-0 p-0">{{ likeMovie.title }}</p>
                    <small>({{ likeMovie.release_date }} 개봉)</small>
                  </div>
                </div>
              </div>
            </div>


            <div v-else class="p-1">
              <p class="m-0">좋아요한 영화가 아직 없습니다.</p>
            </div>
          </div>
        </div>

        <!-- 내가 쓴 게시글(완료) -->
        <div class="d-flex justify-content-center">
        <div :class="['articleBox', 'border', 'rounded-3', 'text-center', isDarkMode ? 'bgCustom-dark' : 'bgCustom']">

            <div class="p-1">
              <p class="fw-bold">내가 쓴 게시글</p>
            </div>
            <hr class="m-0">
            <div v-if="articles.length < 1" class="p-1">
              <p class="m-0">작성한 글이 아직 없습니다.</p>
            </div>

            <div v-else>
              <ProfileArticle v-for="article in articles" :key="article.id" :article="article" />
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 회원정보 변경 및 탈퇴 기능 -->
  <div v-if="isMyProfile" class="d-flex m-2 justify-content-end">
    <button class="btn btn-secondary btn-sm" type="button" data-bs-toggle="modal" data-bs-target="#updatePassword">
      비밀번호 변경
    </button>
    <PasswordUpdate />
    <button type="button" data-bs-toggle="modal" data-bs-target="#signOut"
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
import Swal from "sweetalert2";


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
const likeMovies = ref([])

const profileExist = computed(() => {
  return profile_image.value
})

// 컬렉션 더보기
const moreCollections = () => {
  router.push({
    name: 'userCollection',
    params: { nickname: userStore.nickname },
  })
}

// 좋아요 영화 더보기
const moreMovies = () => {
  router.push({
    name: 'userCollection',
    params: { nickname: userStore.nickname },
  })
}

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
      Swal.fire({
        title: `내 상태 변경이 완료되었습니다.`,
        icon: "success",
        confirmButtonColor: "#3085d6",
        confirmButtonText: "확인"
      })
      updateStatus.value = false
      userStore.userInfo.status = status.value
      location.reload()
    })
}

defineProps({
  isDarkMode:Boolean,
})

const cancleStatus = () => {
  status.value = userStore.userInfo.status
  updateStatus.value = false
}

// 프로필 유저정보 불러오기
onMounted(() => {
  userProfile(profileUserNickname)
    .then((response) => {
      console.log(response.data)
      userInfo.value = response.data
      collections.value = response.data.collections
      likeMovies.value = response.data.like_movies
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
      Swal.fire({
        title: `유저 정보가 존재하지 않습니다.`,
        icon: "success",
        confirmButtonColor: "#dc3545",
        confirmButtonText: "확인"
      })
      router.push({ name: 'home' })
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
.bgCustom {
  background-color: white;
}
.bgCustom-dark {
  background-color: #F6FFE8;
  border: 1px solid lightgray;
  border-radius: 10px;
}
/* .borderCustom {
  border: 5px solid #06bb1e;
} */
p {
  margin: 0;
  padding: 5px 0px;
}

.articleBox {
  width: 92%;
  min-height: 40vh;
}

.myBlogBox {
  min-width: 70vw;
  background-color: #f6ffe8;
}

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

.superTop {
  min-width: 645px;
}

.leftSide {
  max-width: 285px;
}

.minimumBox {
  min-height: 15vw;
  min-width: 220px;
}
</style>