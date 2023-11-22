<template>
  <div class="container">
    <h2>HOT 게시글 모아모아</h2>
    <div class="popular-article my-3">
      <div v-for="article in articles.slice(0, 4)" :key="article.id">
        <CommunityGridCard 
          :article="article"
        />
      </div>
    </div>

    <h2>게시글 목록</h2>
    <div class="latest-article">
      <div v-for="article in articles" :key="article.id">
        <CommunityGridCard
          :article="article"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import CommunityGridCard from '@/components/community/CommunityGridCard.vue';

defineProps({
  articles: Array
})
</script>

<style scoped>
.container {
  max-width: 90%;
}

.popular-article {
  border: 1px solid black;
  background-color: #E0FDED;
}

.latest-article {
  height: 80vh;
  border: 1px solid black;
}
</style>