// movieStore.js
import { defineStore } from 'pinia';
import axios from 'axios';

export const useMovieStore = defineStore({
  id: 'movie',
  state: () => ({
    movies: [],
  }),
  actions: {
    async fetchMovies() {
      const moviesURL = 'http://';
      const options = {
        method: 'GET',
        url: moviesURL,
        params: { language: 'ko-KR', page: '1' },
        headers: {
          accept: 'application/json',
          Authorization: `Bearer ${import.meta.env.VITE_API_KEY}`
        }
      };

      try {
        const response = await axios.request(options);
        this.movies = response.data.results;
      } catch (error) {
        console.error(error);
      }
    },
  },
});
