<template>
  <div class="test-content">
    <h3 class="test-title">평점순</h3>
    <div ref="horizontalScrollWrap" class="horizontal-scroll" @mouseover="pauseScroll" @mouseleave="resumeScroll">
      <ul>
        <template v-for="i in 12" :key="i">
          <li :style="{ backgroundColor: `hsl(${parseInt(Math.random() * 24, 10) * 15}, 16%, 57%)` }"></li>
        </template>
      </ul>
      <template v-for="(chunk, chunkIndex) in infiniteChunks" :key="chunkIndex">
        <MovieCard
          v-for="(movie, index) in chunk"
          :key="index + chunkIndex * chunkSize"
          :movie="movie"
        />
      </template>
    </div>
  </div>
</template>

<script setup>
import MovieCard from '@/components/Movies/MovieCard.vue'
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

const horizontalScrollWrap = ref(null);
const isMouseDown = ref(false);
let startX = 0;
let scrollLeft = 0;
const chunkSize = 3; // 한 번에 보여줄 카드 수
let scrollInterval;

onMounted(() => {
  const wrap = horizontalScrollWrap.value;
  wrap.addEventListener('mousedown', (e) => {
    isMouseDown.value = true;
    startX = e.pageX - wrap.offsetLeft;
    scrollLeft = wrap.scrollLeft;
  });

  wrap.addEventListener('mouseleave', () => {
    isMouseDown.value = false;
  });

  wrap.addEventListener('mouseup', () => {
    isMouseDown.value = false;
  });

  wrap.addEventListener('mousemove', (e) => {
    if (!isMouseDown.value) return;

    e.preventDefault();
    const x = e.pageX - wrap.offsetLeft;
    const beforeScrollLeft = (x - startX) * 1;
    wrap.scrollLeft = scrollLeft - beforeScrollLeft;
  });

  // 자동으로 슬라이딩 시작
  scrollInterval = setInterval(() => {
    wrap.scrollLeft += 1;
  }, 20);
});

const key = import.meta.env.VITE_TMDB_API_KEY;
const movies = ref([]);

const fetchMovie = () => {
  const url = 'https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=1';
  const headers = {
    Accept: 'application/json',
    Authorization: `Bearer ${key}`,
  };

  axios.get(url, { headers })
    .then((response) => {
      movies.value = response.data.results.slice(0, 50);
    })
    .catch((err) => {
      alert('Axios Error: ' + err.message);
    });
};

onMounted(() => {
  fetchMovie();
});

console.log(movies)

const chunkedMovies = ref([]);

watch(() => movies.value, () => {
  chunkedMovies.value = chunkArray(movies.value, chunkSize);
});

function chunkArray(arr, size) {
  const chunkedArr = [];
  for (let i = 0; i < arr.length; i += size) {
    chunkedArr.push(arr.slice(i, i + size));
  }
  return chunkedArr;
}

// MovieCard를 무한으로 반복하기 위한 로직
const infiniteChunks = ref([]);

watch(() => chunkedMovies.value, () => {
  infiniteChunks.value = generateInfiniteChunks(chunkedMovies.value);
});

function generateInfiniteChunks(chunks) {
  const result = [];
  for (let i = 0; i < 3; i++) {
    result.push(...chunks);
  }
  return result;
}

// 좌우 스크롤 버튼 추가
function pauseScroll() {
  clearInterval(scrollInterval);
}

function resumeScroll() {
  // 일정 간격으로 슬라이딩 재개
  scrollInterval = setInterval(() => {
    horizontalScrollWrap.value.scrollLeft += 1;
  }, 20);
}
</script>

<style scoped>
.test-title {
  margin-left: 20px;
  color: white;
}
.test-title {
  margin-left: 20px;
}
.horizontal-scroll {
  display: flex;
  overflow-x: auto;
  width: 100%;
  scrollbar-width: thin; /* Firefox */
  scrollbar-color: transparent transparent; /* Firefox */
  position: relative; /* 추가된 부분 */
}

/* 그라데이션 바와 버튼 고정 위치 조정 */
.gradient-bar {
  width: 20%;
  height: 100%;
  background: linear-gradient(to right, rgba(0, 0, 0, 0.8), transparent);
  opacity: 0.7;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1;
}
.horizontal-scroll::-webkit-scrollbar {
  width: 12px; /* Safari and Chrome */
}

.horizontal-scroll::-webkit-scrollbar-thumb {
  background-color: transparent; /* Safari and Chrome */
}
</style>