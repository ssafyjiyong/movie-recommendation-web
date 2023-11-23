<template>
    <div>
      <div id="articleList" class="d-flex text-center justify-content-between">
        <div class="col-1 py-2">{{ article.id }}</div>
        <div @click="goToDetail(article.id)" class="articleTitle col-7 py-2">{{ article.title }}</div>
        <div class="col-2 py-2">{{ article.user.nickname }}</div>
        <div class="col-2 py-2">{{ formatDate(article.created_at) }}</div>
      </div>
      <hr class="m-0">
    </div>

</template>

<script setup>
import { useRouter } from 'vue-router';

const props = defineProps({
  article: Object,
})

const router = useRouter()


const formatDate = (dateStr) => {
  const date = new Date(dateStr);
  return date.toLocaleDateString('ko-KR', { year: '2-digit', month: '2-digit', day: '2-digit' });
}

const goToDetail = function (articleId) {
  router.push(`/communitydetail/${props.article.category}/${articleId}`)
}

</script>

<style scoped>
#articleList:hover {
  background-color: rgb(248, 248, 248);
  font-weight: bold;
  color: rgb(99, 99, 99);
}

.articleTitle {
  cursor: pointer;
}

.btn-custom {
  background-color: #83C442;
  color: white;
}

.topArticleBox {
  width: 80%;
}

.latest-article {
  min-height: 10vh;
  border: 1px solid #BFBFBF;
  border-start-start-radius: 10px;
  border-start-end-radius: 10px;
}
</style>