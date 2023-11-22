import { createI18n } from 'vue-i18n'
import ko from '@/locales/ko.json'
import en from '@/locales/en.json'

export const i18n = new createI18n({
  locale: 'ko',
  fallbackLocale: 'en',
  messages: {
    'ko': ko,
    'en': en
  }
})