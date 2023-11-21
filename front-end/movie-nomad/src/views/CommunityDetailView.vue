<template>
  <div class="container">
    <div class="article-area">
      <h1>{{ article.title }}</h1>
      <div id='article-info'>
        {{ article.user['nickname'] }} | {{ article.movie }} | 마지막 수정일 : {{ article.updated_at.substr(0, 10) }}
      </div>
      <hr>
      <p>{{ article.content }}</p>
    </div>
    <div class="comment-area">
      <h1>comment</h1>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router'
import { useArticleStore } from '@/stores/article';

const props = defineProps({
  article: Object
})
const store = useArticleStore()
const route = useRoute()

const article = ref(store.article)

onMounted(() => {
  // store.articleDetail(route.params.articleId)
})

</script>

<style scoped>
.container {
  max-width: 90%;
}

.article-area {
  border: 1px black solid;
  border-radius: 10px;
  margin-top: 30px;
  padding: 20px;
}

.comment-area {
  border: 1px solid black;
  border-radius: 10px;
  margin-top: 30px
}

#article-info {
  text-align: right;
}
</style>