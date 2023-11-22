<template>
  <div>
    <h1>배리어프리</h1>
  </div>

  <div class="latest-article">
    <div v-for="article in articles" :key="article.id">
      <CommunityGridCard :article="article" />
    </div>
  </div>
</template>

<script setup>
defineProps({
  isDarkMode:Boolean,
})

</script>

<style scoped>
.latest-article {
  height: 80vh;
  border: 1px solid black;
}
</style>