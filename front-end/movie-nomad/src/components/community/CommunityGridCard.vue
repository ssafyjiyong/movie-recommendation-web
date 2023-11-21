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
import { useArticleStore } from '@/stores/article';
import { onMounted } from 'vue';

const store = useArticleStore()
const props = defineProps({
  article: Object
})


onMounted(() => {
  const article = store.articleDetail(props.article.id)
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