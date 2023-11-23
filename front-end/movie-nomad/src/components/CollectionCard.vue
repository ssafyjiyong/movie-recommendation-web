<template>
  <div>
    <h3 class="collection-name">{{ collection.name }}</h3>
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
import { ref, onMounted } from 'vue';
import { getMoviesList } from '@/apis/movieApi';

const props = defineProps({
  collection: Object
})

const movies = ref([])

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
})
</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}

.collection-name {
  padding: 10px 20px;
  margin: 0;
  color: white;
  background-color: #83C442;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.movie-list {
  border-radius: 10px;
  background-color: #F6FFE8;
  padding: 20px;
  margin: 0 0 20px 0;
  text-align: center;
}

.movie-poster img{
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