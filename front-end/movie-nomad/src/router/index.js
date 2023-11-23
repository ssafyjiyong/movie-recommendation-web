import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MoviesView from '@/views/MoviesView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import CommunityDetailView from '@/views/CommunityDetailView.vue'
import CommunityNavView from '@/views/CommunityNavView.vue'
import ProfileView from '@/views/ProfileView.vue'
import CommunityView from '@/views/CommunityView.vue'


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
      path: '/moviedetail/:movieId',
      name: 'moviedetail',
      component: MovieDetailView
    },
    {
      path: '/community',
      name: 'communitynav',
      component: CommunityNavView,
      children: [
        {
          path: '/community/:category',
          name: 'community',
          component: CommunityView
        },
        {
          path: '/communitydetail/:category/:articleId',
          name: 'communityDetail',
          component: CommunityDetailView
        },
      ]
    },
    {
      path: '/profile/:nickname',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/LoginView.vue')
    },
    {
      path: '/create/:category',
      name: 'create',
      component: () => import('@/views/CommunityCreate.vue')
    },
    {
      path: '/community/update/:articleId/:category',
      name: 'communityupdate',
      component: () => import('@/views/CommunityUpdate.vue')
    },
    {
      path: '/passwordchange',
      name: 'passwordChange',
      component: () => import('@/views/PasswordChangeView.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('@/views/SignupView.vue')
    },
  ]
})

export default router
