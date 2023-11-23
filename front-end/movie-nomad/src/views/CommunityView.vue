<template>
  <div class="topTopBox">
    <div class="theTopBox">
      <div class="d-flex justify-content-between">
      <div class="m-3">
        <i class="fa-solid fa-comment-dots fa-lg mx-2"></i><span class="fw-bold textColor">{{ category }}</span>
      </div>
      <div>
          <button class="btn btn-custom btn-sm fw-bold mt-3 me-3" @click="goToAddArticle">글쓰기</button>
        </div>
      </div>

      <CommunityGrid 
      :allArticles="allArticles"/>

    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { getArticlesList } from '@/apis/movieApi';
import CommunityGrid from '@/components/community/CommunityGrid.vue';
import { computed } from '@vue/reactivity';

defineProps({
  isDarkMode: Boolean,
})

const router = useRouter()
const route = useRoute()
const allArticles = ref([])

const category = computed(()=> {
  if (route.params.category==='talk') {
  return '영화토크'
} else if (route.params.category==='toon') {
  return '영화툰'
} else if (route.params.category==='ticket') {
  return '티켓나눔'
} else if (route.params.category==='preview') {
  return '영화뉴스'
} else {
  return '배리어프리'
}
})

const goToAddArticle = function () {
  router.push('/create/1/')
}

onMounted(async () => {
  await getArticlesList()
    .then(response => {
      allArticles.value = response.data.filter((article) => {
        return article.category === 'talk'
      })
    })
});
</script>

<style scoped>
#articleList:hover {
  background-color: rgb(248, 248, 248);
  font-weight: bold;
  color: rgb(99, 99, 99);
}
.topTopBox {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.theTopBox {
  width: 800px;
  display: flex;
  flex-direction: column;
}
.textColor {
  color: rgb(37, 37, 37);
}

.btn-custom {
  background-color: #83C442;
  color: white;
}

/* 미디엄사이즈 */
@media only screen and (max-width: 768px) {

.topTopBox {
  justify-content:start;
  margin: auto 5px;
}
}

/* 스몰사이즈 */
@media only screen and (max-width: 576px) {

  .theTopBox,
  .topTopBox {
    justify-content:start;
    margin: auto 5px;
  }
}
</style>