<template>
  <!-- Navigation-->
  <div class="theTopBox">
    <nav class="communityNav m-3 py-1">
      <ul class="d-flex justify-content-center align-items-center m-0 p-0">
        <li>
          <RouterLink class="text-decoration-none text-white fw-bold" to="/community/talk">영화토크</RouterLink>
        </li>
        <li>
          <RouterLink class="text-decoration-none text-white fw-bold" to="/community/toon">영화툰</RouterLink>
        </li>
        <li>
          <RouterLink class="text-decoration-none text-white fw-bold" to="/community/ticket">티켓나눔</RouterLink>
        </li>
        <li>
          <RouterLink class="text-decoration-none text-white fw-bold" to="/community/preview">영화뉴스</RouterLink>
        </li>
        <li>
          <RouterLink class="text-decoration-none text-white fw-bold" to="/community/barrier">배리어프리</RouterLink>
        </li>
      </ul>
    </nav>
  </div>

  <RouterView class="d-grid" />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

defineProps({
  isDarkMode: Boolean,
})

</script>

<style scoped>
.theTopBox {
  display: flex;
  justify-content: center;
}

ul {
  list-style: none;
}

ul>li {
  padding: 10px;
  margin: 0px 10px;

}

.communityNav {
  width: 800px;
  background-color: rgb(131, 196, 66);
  border-radius: 50px;
}

/* 스몰사이즈 */
@media only screen and (max-width: 576px) {
  .theTopBox {
    display: block;
  }
}
</style>