<template>
  <div>
    <div class="collection-name">
      <h3>{{ collection.name }}</h3>
      <div v-show="myCollection">
        <button @click="deleteCollection" class="btn btn-danger btn-sm">컬렉션 삭제</button>
      </div>
    </div>
    <div class="movie-list row row-cols-auto">
      <div class="col-sm-4 col-md-3 col-lg-2" v-for="movie in movies" :key="movie.id">
        <RouterLink class="movie-poster" :to="{ name: 'moviedetail', params: { movieId: movie.pk } }">
          <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="poster">
          <div class="title-box">
            <h6 class="movie-title">{{ movie.title }}</h6>
          </div>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useUserStore } from '@/stores/userStore';
import { getMoviesList, deleteCollectionApi } from '@/apis/movieApi';

const userStore = useUserStore()

const props = defineProps({
  collection: Object
})

const mine = () => {
  if (userStore.userData.pk === props.collection.user) {
    myCollection.value = true
  } else {
    myCollection.value = false
  }
}

const myCollection = ref(false)

const movies = ref([])

const deleteCollection = () => {
  deleteCollectionApi(props.collection.id)
    .then((response) => {
      window.alert("삭제되었습니다.")
      location.reload()
    })
}


onMounted(() => {
  getMoviesList()
    .then(response => {
      props.collection.movie.forEach(pk => {
        const movie = response.data.find(movie => movie.pk === pk);
        // console.log(movie);
        if (movie) {
          movies.value.push(movie);
        }
      });
    })
    .then(() => {
      mine()
    })
})
</script>

<style scoped>
a {
  text-decoration: none;
}

.collection-name {
  padding: 10px 20px;
  margin: 0;
  color: white;
  background-color: #83C442;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  display: flex;
  justify-content: space-between;
}

.movie-list {
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  background-color: #F6FFE8;
  padding: 20px;
  margin: 0 0 20px 0;
  text-align: center;
}

.movie-poster img {
  width: 100%;
  height: 80%;
  margin-bottom: 10px;
}

.title-box {
  margin-bottom: 10px;
}

.movie-title {
  color: #83C442;
}
</style>