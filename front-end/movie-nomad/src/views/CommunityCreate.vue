<template>
  <div>
    <h1>CommunityCreate</h1>
    <form>
      <div class="form-check">
        <input class="form-check-input" type="radio" name="flexRadioDefault" 
        id="talk" 
        value="talk"
        v-model="category"
        >
        <label class="form-check-label" for="talk">
          영화토크
        </label>
      </div>
      <div class="form-check">
        <input class="form-check-input" type="radio" name="flexRadioDefault" 
        id="toon" 
        value="toon"
        v-model="category"
        >
        <label class="form-check-label" for="toon">
          영화툰
        </label>
      </div>
      <div class="form-check">
        <input class="form-check-input" type="radio" name="flexRadioDefault" 
        id="ticket"
        value="ticket"
        v-model="category"
        >
        <label class="form-check-label" for="ticket"> 
          티켓나눔
        </label>
      </div>

      <label for="movie">movie :</label>
      <input type="text" id="movie" v-model="movieid">


      <label for="title">글제목 : </label>

      <input type="text" id="title" v-model="title">

    </form>
    <form>
      <label for="content"></label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
    </form>
  </div>

  <button @click="addArticle">게시글 생성하기</button>
</template>

<script setup>
import { useArticleStore } from '@/stores/articleStore';
import { useMovieStore } from '@/stores/movieStore';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

defineProps({
  isDarkMode:Boolean,
})

const route = useRoute()

const articleNumber = route.params.category;
const categoryMap = ['talk', 'toon', 'ticket'];

const articleStore = useArticleStore()
const movieStore = useMovieStore()

const category = ref(categoryMap[articleNumber - 1])
const movieid = ref(null)
const title = ref(null)
const content = ref(null)

const addArticle = function () {
  const payload = {
    category: category.value,
    movie: movieid.value,
    title: title.value,
    content: content.value
  }
  articleStore.createArticle(payload)
}

onMounted(() => {
  movieStore.initializeMovies()
});

</script>

<style scoped></style>