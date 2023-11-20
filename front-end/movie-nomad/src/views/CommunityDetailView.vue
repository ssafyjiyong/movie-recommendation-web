<template>
  <div class="container">
    <div class="article">
      <h1>{{ article.title }}</h1>
    </div>
    <div class="comment">
      <h1>comment</h1>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router'
import { useArticleStore } from '@/stores/article';

const store = useArticleStore()
const route = useRoute()

const article = ref(store.article)

onMounted(() => {
  store.articleDetail(route.params.articleId)
})

</script>

<style scoped>
.container {
  max-width: 90%;
}

.article {
  height: 40vh;
  border: 1px black solid;
  border-radius: 10px;
}
</style>