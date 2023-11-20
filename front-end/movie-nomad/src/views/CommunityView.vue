<template>
  <!-- Navigation-->
  <nav class="communityNav">
    <ul class="d-flex justify-content-around align-items-center">
      <li><RouterLink to="/talk">영화토크</RouterLink></li>
      <li><RouterLink to="/toon">영화툰</RouterLink></li>
      <li><RouterLink to="/ticket">티켓나눔</RouterLink></li>
      <li><RouterLink to="/preview">영화뉴스</RouterLink></li>
      <li><RouterLink to="/barrier">베리어프리</RouterLink></li>
    </ul>
  </nav>

  <RouterView />
  
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>
ul {
   list-style:none;
   margin: 0;
   padding: 0;
   }

ul > li {
   padding: 10px;
   border: 1px solid red;
   }
.communityNav {
  margin: 10px 100px;
  border: 1px solid red;
}
</style>