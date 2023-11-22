<template>
  <div class="container">
    <!-- <h2>HOT 게시글 모아모아</h2>
    <div class="popular-article my-3">
      <div v-for="article in articles.slice(0,5)" :key="article.id">
        <CommunityGridCard 
          :article="article"
        />
      </div>
    </div> -->

    <h2>게시글 목록</h2>
    <div class="latest-article">
      <!-- 게시글 -->
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
import { ref, computed } from 'vue';
import { sortBy } from 'lodash';

const props = defineProps({
  articles: Array
})

// const hotArticles = computed(() => sortBy(props, 'like_user_count').reverse().slice(0, 4));
// console.log(props)
// console.log(hotArticles.value)

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