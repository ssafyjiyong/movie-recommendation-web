<template>
  <div class="container mt-3">
    <div class="row justify-content-center">
      <div class="col-md-8">

        <div class="text-center p-3">
          <h2>글 작성하기</h2>
        </div>
        
        <form @submit.prevent="addArticle">
          <div class="mb-3">게시판</div>
          <div class="d-flex justify-content-around mb-3">
            <div class="form-check">
              <input class="form-check-input" type="radio" name="flexRadioDefault" id="talk" value="talk"
                v-model="category">
              <label class="form-check-label" for="talk">
                영화토크
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="flexRadioDefault" id="toon" value="toon"
                v-model="category">
              <label class="form-check-label" for="toon">
                영화툰
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="flexRadioDefault" id="ticket" value="ticket"
                v-model="category">
              <label class="form-check-label" for="ticket">
                티켓나눔
              </label>
            </div>
          </div>

          <div class="mb-3">
            <label for="movie" class="form-label">영화 선택 :</label>
            <input v-model="movieid" class="form-control" list="movieOptions" id="movie" placeholder="영화 제목을 검색해주세요">
            <datalist v-if="allMovies.length" id="movieOptions">
              <option v-for="(movie, idx) in allMovies" :key="idx" :value="movie.pk">{{ movie.title }}</option>
            </datalist>
          </div>

          <div class="mb-3">
            <label for="title" class="form-label">글 제목 :</label>
            <input v-model="title" type="text" class="form-control" id="title" />
          </div>

          <div class="mb-3">
            <label for="content" class="form-label">글 내용 :</label>
            <textarea class="form-control" id="content" rows="10" v-model="content"></textarea>
          </div>

          <div class="mb-3">
            <label for="image" class="form-label">이미지 업로드</label>
            <input @change="uploadFiles" class="form-control" accept="image/*" type="file" id="image">
          </div>


          <div class="d-grid mb-4">
            <button type="submit" class="btn btn-custom fw-bold">게시글 생성하기</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/articleStore';
import { useMovieStore } from '@/stores/movieStore';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute()

const articleNumber = route.params.category;
const categoryMap = ['talk', 'toon', 'ticket'];

const articleStore = useArticleStore()
const movieStore = useMovieStore()

const category = ref(categoryMap[articleNumber - 1])
const movieid = ref(null)
const title = ref(null)
const content = ref(null)
const articleImage = ref([])
const allMovies = ref([]);

const uploadFiles = (event) => {
  for (let file of event.target.files) {
    articleImage.value.push(file);
  }
};

const addArticle = function () {
  const payload = {
    category: category.value,
    movie: movieid.value,
    title: title.value,
    content: content.value,
    image: articleImage.value[0],
  }
  articleStore.createArticle(payload)
}

onMounted(async () => {
  await movieStore.initializeMovies()
  console.log(movieStore.allMovies)
  allMovies.value = movieStore.allMovies
});

</script>

<style scoped>
.btn-custom {
  background-color: #83C442;
  color: white;
}
</style>