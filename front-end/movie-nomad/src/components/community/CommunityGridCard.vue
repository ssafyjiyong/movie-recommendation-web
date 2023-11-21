<template>
  <div>
    <RouterLink :to="{ name: 'communityDetail', params: { articleId: article.id } }" :article="article">
      <span class="article-title">{{ article.title }}</span>
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { onMounted } from 'vue';
import { getArticleDetail } from '@/apis/movieApi'

const props = defineProps({
  article: Object
})


onMounted(() => {
  getArticleDetail(props.article.id)
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