import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
const TMDB_URL_POPULAR = 'https://api.themoviedb.org/3/movie/popular?language=en-US&page=1'
const TMDB_URL_UPCOMING = 'https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1'
const TMDB_URL_NOWPLAYING = 'https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1'
const TMDB_KEY = import.meta.env.VITE_TMDB_API_KEY

// POPULAR 영화 API
export const getPopularMovies = () => {
  const headers = {
    accept: 'application/json',
    Authorization: `Bearer ${TMDB_KEY}`
  }
  return axios
    .get(TMDB_URL_POPULAR, { headers })
    .then((response) => {
      return response
    })
    .catch((err) => {
      console.error('POPULAR, Axios Error:', err.message)
      throw err
    })
}

// UPCOMING 영화 API
export const getUpcomingMovies = () => {
  const headers = {
    accept: 'application/json',
    Authorization: `Bearer ${TMDB_KEY}`
  }
  return axios
    .get(TMDB_URL_UPCOMING, { headers })
    .then((response) => {
      return response
    })
    .catch((err) => {
      console.error('UPCOMING, Axios Error:', err.message)
      throw err
    })
}

// NOW PLAYING 영화 API
export const getNowPlayingMovies = () => {
  const headers = {
    accept: 'application/json',
    Authorization: `Bearer ${TMDB_KEY}`
  }
  return axios
    .get(TMDB_URL_NOWPLAYING, { headers })
    .then((response) => {
      return response
    })
    .catch((err) => {
      console.error('NOW PLAYING, Axios Error:', err.message)
      throw err
    })
}

// 영화 List 전체 조회 API
export const getMoviesList = () => {
  return axios.get(`${API_URL}/movies/movielist/`)
}

// 영화 검색 API
export const searchMovie = (movieKeyword) => {
  return axios.get(`${API_URL}/movies/movie_search/${movieKeyword}/`)
}

// 단일 영화 상세 조회 API
export const getMovieDetail = (moviePk) => {
  return axios.get(`${API_URL}/movies/movie_detail/${moviePk}/`)
}


// 영화 좋아요 API
export const likeMovieApi = (moviePk) => {
  const token = window.localStorage.getItem('token')
  return axios
    .post(
      `${API_URL}/movies/movie_detail/${moviePk}/like/`,
      {
        headers: {
          Authorization: `Token ${token}`
        }
      }
    )
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('영화 좋아요, API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 영화 그저그래요 API
export const sosoMovieApi = (moviePk) => {
  const token = window.localStorage.getItem('token')
  return axios
    .post(
      `${API_URL}/movies/movie_detail/${moviePk}/soso/`,
      {
        headers: {
          Authorization: `Token ${token}`
        }
      }
    )
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('영화 그저그래요, API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 영화 별로예요 API
export const hateMovieApi = (moviePk) => {
  const token = window.localStorage.getItem('token')
  return axios
    .post(
      `${API_URL}/movies/movie_detail/${moviePk}/hate/`,
      {
        headers: {
          Authorization: `Token ${token}`
        }
      }
    )
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('영화 별로예요, API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}


// 여기서부터 커뮤니티 관련입니다---------------------------------------------------------------------------------


// 게시글 List 전체 조회 API
export const getArticlesList = () => {
  return axios.get(`${API_URL}/article_list/`)
}

// 영화 디테일 페이지 해당 영화 article List 조회
export const thisMovieArticles = (moviePk) => {
  return axios
    .get(`${API_URL}/article_list/${moviePk}/`)
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('해당 영화 article List, API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 단일 게시글 조회
export const getArticleDetail = (articlePk) => {
  return axios
    .get(`${API_URL}/article_detail/${articlePk}/`)
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('단일 게시글, API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 게시글 작성 API
export const createArticleAPI = (payload) => {
  const token = window.localStorage.getItem('token')
  return axios
    .post(`${API_URL}/article_list/${moviePk}/`, payload, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('게시글 작성, API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 게시글 삭제 API
export const deleteArticleAPI = (articlePk) => {
  const token = window.localStorage.getItem('token')
  return axios
    .delete(`${API_URL}/article_detail/${articlePk}/`, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('게시글 삭제, API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 게시글 수정 API
export const updateArticleAPI = (articlePk, payload) => {
  const token = window.localStorage.getItem('token')
  return axios
    .put(`${API_URL}/article_detail/${articlePk}/`, payload, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('게시글 수정, API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}


// 여기서부터 코멘트 관련입니다---------------------------------------------------------------------------------


// 단일 게시글 comment List 조회
export const getCommentList = (articlePk) => {
  return axios
    .get(`${API_URL}/article_detail/${articlePk}/comment/`)
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('코멘트 조회, API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}


// 단일 게시글 comment 작성
export const createCommentAPI = (articlePk, payload) => {
  const token = window.localStorage.getItem('token')
  return axios
    .post(`${API_URL}/article_detail/${articlePk}/comment/`, payload, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('comment 작성, API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// comment 삭제
export const deleteCommentAPI = (articlePk, commentPk) => {
  const token = window.localStorage.getItem('token')
  return axios
    .delete(`${API_URL}/article_detail/${articlePk}/comment/${commentPk}`, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('comment 삭제, API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 단일 게시글 좋아요 API
export const likeArticleApi = (articlePk) => {
  const token = window.localStorage.getItem('token')
  return axios
    .post(
      `${API_URL}/article_detail/${articlePk}/article_like/`,
      {},
      {
        headers: {
          Authorization: `Token ${token}`
        }
      }
    )
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}
