<template>
  <div class="wrap"> <!-- 배너표시영역 -->
    <div class="rolling-list"> <!-- 원본배너 -->
      <ul>
        <li v-for="poster in posters" :key="poster.id">
          <img :src="`https://image.tmdb.org/t/p/w500/${poster}`" alt="movie_poster" class="posterImage">
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useMovieStore } from '@/stores/movieStore';

const movieStore = useMovieStore()
const posters = ref(movieStore.popularMovieImages)

onMounted(() => {
  movieStore.getCarouselImages()
});

// 롤링 배너 복제본 생성
let roller = document.querySelector('.rolling-list');
roller.id = 'roller1'; // 아이디 부여

let clone = roller.cloneNode(true)
// cloneNode : 노드 복제. 기본값은 false. 자식 노드까지 복제를 원하면 true 사용
clone.id = 'roller2';
document.querySelector('.wrap').appendChild(clone); // wrap 하위 자식으로 부착

document.querySelector('#roller1').style.left = '0px';
document.querySelector('#roller2').style.left = document.querySelector('.rolling-list ul').offsetWidth + 'px';
// offsetWidth : 요소의 크기 확인(margin을 제외한 padding값, border값까지 계산한 값)

roller.classList.add('original');
clone.classList.add('clone');
</script>

<style scoped>
.poster-slide {
  display: flex;
  flex-direction: row;
}
</style>
