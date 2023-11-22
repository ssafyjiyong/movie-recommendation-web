<template>
  <div class="container">
    <h1>HOT 게시글 모아모아</h1>
    <div class="popular-article">
      <div v-for="article in articles.slice(0, 4)" :key="article.id">
        <CommunityGridCard 
          :article="article"
        />
      </div>
    </div>

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
  height: 172px;
  border: 1px solid black;
  border-radius: 10px;
  background-color: #E0FDED;
  padding-top: 13px;
}

.latest-article {
  height: 1300px;
  margin-top: 20px;
  border: 1px solid black;
  border-radius: 10px;
  padding-top: 13px;

}
</style>