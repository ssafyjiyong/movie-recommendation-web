<template>

<div class="topArticleBox">
        <div class="latest-article">
          <div class="articleBox d-flex text-center justify-content-between">
            <div class="col-1 py-3">번호</div>
            <div class="col-7 py-3">글제목</div>
            <div class="col-2 py-3">작성자</div>
            <div class="col-2 py-3">작성일</div>
          </div>
          <hr class="m-0">

          <CommunityGridCard 
          :allArticles="allArticles"/>

        </div>
      </div>
</template>

<script setup>
import CommunityGridCard from './CommunityGridCard.vue';
import { ref } from 'vue';

defineProps({
  allArticles:Array,
})

const allArticles = ref([])

</script>

<style scoped>

.topArticleBox {
  width: 78%;
}

.latest-article {
  min-height: 10vh;
  border: 1px solid #BFBFBF;
  border-start-start-radius: 10px;
  border-start-end-radius: 10px;
}
</style>