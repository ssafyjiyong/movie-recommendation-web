<template>
  <header>
    <!-- Navigation-->
    <nav class="navbar navbar-expand-md navbar-light" id="mainNav">
      <div class="container-fluid px-2 px-lg-3">
        <div v-if="!isDarkMode">
          <RouterLink to="/"><img src="@/images/logo_without_bg.png" alt="logo_image"></RouterLink>
        </div>
        <div v-else>
          <RouterLink to="/"><img src="@/images/logo_without_bg_dark.png" alt="logo_image"></RouterLink>
        </div>
        <button class="navbar-toggler border border-0" type="button" data-bs-toggle="collapse"
          data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
          aria-label="Toggle navigation">
          <i class="fas fa-bars fa-xl py-3"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ms-auto text-center align-items-center">
            <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2">


                  <button class="btn btn-link" @click="$i18n.locale = 'ko'"> 한국어 </button>
                  <button class="btn btn-link" @click="$i18n.locale = 'en'"> English </button>
              
            </li>
            <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2">
              <button :class="['btn', 'btn-link', isDarkMode ? 'text-white' : 'text-black']" @click="toggleDarkMode">
                <!-- 다크모드일 경우 아이콘 -->
                <div v-if="isDarkMode">
                  <i class="fa-regular fa-lightbulb"></i>
                </div>
                <!-- 일반모드 아이콘 -->
                <div v-else>
                  <i class="fa-solid fa-lightbulb"></i>
                </div>
              </button>
            </li>
            <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2" @click="goToMovieList">
              {{ $t('movieList') }}

            </li>

            <div v-if="!userStore.isLogin" class="d-flex">
              <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2">
                <RouterLink :to="{ name: 'login' }">{{ $t('Login') }}</RouterLink>
              </li>
              <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2">
                <RouterLink :to="{ name: 'signup' }">{{ $t('Signup') }}</RouterLink>
              </li>
            </div>

            <div v-else class="d-flex justify-content-center align-items-center">
              <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2">
                <RouterLink :to="{ name: 'profile', params: { nickname: userStore.userInfo.nickname } }">{{
                  userStore.userInfo.nickname }}</RouterLink>
              </li>
              <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2">
                <a @click="logout">{{ $t('Logout') }}</a>
              </li>
            </div>
          </ul>
        </div>
      </div>
    </nav>

    <RouterView
    :isDarkMode="isDarkMode" />

  </header>

  <!-- Footer-->
  <footer class="border-top px-2 py-3">
    <div class="container-fluid d-flex justify-content-between">
      <div>
        <div class="small text-muted fs-6">TEAM Making A Different</div>
        <div class="small text-muted fst-italic">Copyright &copy; Team M.A.D All Rights Reserved.</div>
      </div>
      <div>
        <a href="#!">
          <span class="fa-stack fa-lg">
            <i class="fas fa-circle fa-stack-2x text-secondary"></i>
            <i class="fa-regular fa-envelope fa-stack-1x fa-inverse"></i>
          </span>
        </a>
        <a href="#!">
          <span class="fa-stack fa-lg">
            <i class="fas fa-circle fa-stack-2x text-secondary"></i>
            <i class="fab fa-github fa-stack-1x fa-inverse"></i>
          </span>
        </a>
        <a href="#!">
          <span class="fa-stack fa-lg">
            <i class="fas fa-circle fa-stack-2x text-secondary"></i>
            <i class="fa-solid fa-mug-hot fa-stack-1x fa-inverse"></i>
          </span>
        </a>
      </div>
    </div>
  </footer>
</template>


<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/userStore';
import { ref, onMounted, onUnmounted } from 'vue';

const router = useRouter()
const userStore = useUserStore()
const isDarkMode = ref(false);

const logout = () => {
  userStore.logout()
  location.reload()
}

const enableDarkMode = () => {
  document.body.classList.add('dark');
  isDarkMode.value = true;
};

const disableDarkMode = () => {
  document.body.classList.remove('dark');
  isDarkMode.value = false;
};

const toggleDarkMode = () => {
  if (isDarkMode.value) {
    disableDarkMode();
  } else {
    enableDarkMode();
  }
};

const goToMovieList = function () {
  router.push('/movies')
}

onMounted(() => {
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    enableDarkMode();
  };
});

onUnmounted(() => {
  disableDarkMode();
});

</script>


<!-- 전역 스타일 지정 -->
<style>
:root {
  --bg-color: #ffffff;
  --text-color: #000000;
}

body.dark {
  --bg-color: #272727;
  --text-color: #ffffff;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
}
</style>

<!-- 로컬 스타일 지정 -->
<style scoped>
nav {
  font-family: 'Nanum Gothic', sans-serif;
  /* font-family: 'Open Sans', sans-serif; */
  /* font-family: 'Lora', serif; */
  /* font-family: 'Lato', sans-serif; */
}



img {
  width: 250px;
}
</style>
