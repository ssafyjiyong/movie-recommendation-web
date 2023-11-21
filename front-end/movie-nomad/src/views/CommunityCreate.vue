<template>
  <div>
    <h1>CommunityCreate</h1>
    <form>
      <div class="form-check">
        <input class="form-check-input" type="radio" name="flexRadioDefault" 
        id="talk" 
        value="수다"
        v-model="category">
        <label class="form-check-label" for="talk">
          영화토크
        </label>
      </div>
      <div class="form-check">
        <input class="form-check-input" type="radio" name="flexRadioDefault" 
        id="toon" 
        value="영화툰"
        v-model="category">
        <label class="form-check-label" for="toon">
          영화툰
        </label>
      </div>
      <div class="form-check">
        <input class="form-check-input" type="radio" name="flexRadioDefault" 
        id="ticket"
        value="나눔"
        v-model="category">
        <label class="form-check-label" for="ticket"> 
          티켓나눔
        </label>
      </div>

      <label for="movie">movie</label>
      <select name="movie" id="movie" v-model="movieid">
        <option 
        v-for="movie in movieStore.allMovies" 
        :key ="movie.pk"
        :value="movie.pk">{{ movie.title }}</option>
      </select>

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
import { ref } from 'vue';

const articleStore = useArticleStore()
const movieStore = useMovieStore()

const category = ref(null)
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

</script>

<style scoped></style>