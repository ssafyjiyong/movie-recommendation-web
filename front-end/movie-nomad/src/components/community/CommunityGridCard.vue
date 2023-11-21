<template>
  <div>
    <RouterLink :to="{ name: 'communityDetail', params: { articleId: article.id } }">
      <span class="article-title">{{ article.title }}</span>
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { useArticleStore } from '@/stores/article';
import { onMounted, ref } from 'vue';

const store = useArticleStore()
const props = defineProps({
  article: Object
})

</script>

<style scoped>
a {
  text-decoration: none;
}

.article-title {
  font-size: 17px;
  margin-left: 10px;
  color: black;
}
</style>