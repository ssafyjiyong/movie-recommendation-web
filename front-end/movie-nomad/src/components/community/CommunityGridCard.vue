<template>
  <div class="articleBox d-flex justify-content-between">
    <div>{{ article.id }}</div>
    <div>{{ article.title }}</div>
    <div>{{ article.user.nickname }}</div>
    <div>{{ formatDate(article.created_at) }}</div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { onMounted } from 'vue';
import { getArticleDetail } from '@/apis/movieApi'

const props = defineProps({
  article: Object
})

const formatDate = (dateStr) => {
  const date = new Date(dateStr);
  return date.toLocaleDateString('ko-KR', { year: '2-digit', month: '2-digit', day: '2-digit' });
}

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
.articleBox {
  border: 1px solid black;
}
</style>