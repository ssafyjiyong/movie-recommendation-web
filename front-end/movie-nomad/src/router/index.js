import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MoviesView from '@/views/MoviesView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import CommunityDetailView from '@/views/CommunityDetailView.vue'
import CommunityView from '@/views/CommunityView.vue'
import ProfileView from '@/views/ProfileView.vue'
import TalkView from '@/views/TalkView.vue'
import ToonView from '@/views/ToonView.vue'
import TicketView from '@/views/TicketView.vue'
import PreviewInfoView from '@/views/PreviewInfoView.vue'
import BarrierView from '@/views/BarrierView.vue'

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
      name: 'community',
      component: CommunityView,
      children: [
        {
          path: '/talk',
          component: TalkView
        },
        {
          path: '/toon',
          name: 'toon',
          component: ToonView
        },
        {
          path: '/ticket',
          name: 'ticket',
          component: TicketView
        },
        {
          path: '/preview',
          name: 'preview',
          component: PreviewInfoView
        },
        {
          path: '/barrier',
          name: 'barrier',
          component: BarrierView
        },
        {
          path: '/communitydetail/:articleId',
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
