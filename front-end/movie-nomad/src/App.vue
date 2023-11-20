<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <!-- Navigation-->
    <nav class="navbar navbar-expand-md navbar-light" id="mainNav">
      <div class="container-fluid px-2 px-lg-3">
        <RouterLink to="/"><img src="@/images/logo_with_bg.png" alt="logo_image"></RouterLink>
        <button class="navbar-toggler border border-0" type="button" data-bs-toggle="collapse"
          data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
          aria-label="Toggle navigation">
          <i class="fas fa-bars fa-xl py-3"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ms-auto text-center">
            <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2">English</li>
            <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2">다크모드</li>
            <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2">단축키모드</li>
            <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2"><RouterLink :to="{ name: 'login'}">로그인</RouterLink></li>
            <li class="nav-item px-lg-3 py-2 py-lg-2 mx-2"><RouterLink :to="{ name: 'signup' }">회원가입</RouterLink></li>
          </ul>
        </div>
      </div>
    </nav>
    

  <RouterView />

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

<!-- 전역 스타일 지정 -->
<style></style>

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
