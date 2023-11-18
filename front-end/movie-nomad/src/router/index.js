import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MoviesView from '@/views/MoviesView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import CommunityDetailView from '@/views/MovieDetailView.vue'
import CommunityView from '@/views/MovieDetailView.vue'
import ProfileView from '@/views/MovieDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/movies',
      name: 'movies',
      component: MoviesView
    },
    {
      path: '/moviedetail',
      name: 'moviedetail',
      component: MovieDetailView
    },
    {
      path: '/communitydetail',
      name: 'communitydetail',
      component: CommunityDetailView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/LoginView.vue')
    },
    {
      path: '/create',
      name: 'create',
      component: () => import('@/views/CommunityCreate.vue')
    },
    {
      path: '/community/update',
      name: 'communityupdate',
      component: () => import('@/views/CommunityUpdate.vue')
    },
    {
      path: '/passwordchange',
      name: 'passwordchange',
      component: () => import('@/views/PasswordChangeView.vue')
    },
    {
      path: '/profile/update',
      name: 'profileupdate',
      component: () => import('@/views/ProfileUpdateView.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('@/views/SignupView.vue')
    },
  ]
})

export default router
