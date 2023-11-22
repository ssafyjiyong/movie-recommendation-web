import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { getMoviesList, searchMovie } from '@/apis/movieApi'

export const useMovieStore = defineStore('movie', () => {
  // 로딩 메세지
  const loadingMessage = ['행복한지 따져보는 건 우울해지는 지름길이야. - 우리의 20세기',
    '넌 도전했고 도전에는 용기가 필요하지, 네가 자랑스럽구나. - 리틀 미스 선샤인 (Little Miss Sunshine)',
    '운명이란 말야, 노력하는 사람한테 우연이라는 다리를 놓아주는 거야. - 엽기적인 그녀',
    '천재성은 인종은 없고 강인함에는 남녀가 없으며 용기에는 한계가 없다. - 히든 피겨스 (Hidden Figures)',
    '길은 모두에게 열려있지만 모두가 그 길을 가질 수 있는 건 아니다. - 인턴',
    '폭력으로는 절대 이기지 못합니다. 품위를 유지할 때만 이길 수 있는 겁니다. - 그린 북 (Green Book)',
    '단지 두려움 때문에 좋아하는 일을 포기하지 마. - 씽 (Sing)',
    '우리가 앞서 나갈 기회를 잡으면 저들이 결승점을 옮겨놔. - 히든 피겨스',
    '당신을 관두는 법을 알았으면 좋겠어요. - 브로크백 마운틴 (Brokenback Mountain)',
    '호의가 계속되면 그게 권리인 줄 알아. - 부당거래',
    '인생은 다시 돌아올 두 번의 기회가 없다고 생각하고 살아야 해. - 어바웃 타임',
    '알 이즈 웰(All is well) : 모든 게 잘될 거야. - 세 얼간이',
    '네 잘못이 아니야. - 굿 윌 헌팅',
    '벗을 알면 내가 더 깊어진다. - 자산어보',
    '내 아이들에게 부당함을 참으라고 가르치지 않았다. - 필라델피아',
    '사람과 사람의 관계가 시작되는 건, 서로 다름을 인정하는 것부터이다. - 완벽한 타인',
    '인생을 바꿀 기회는 1분마다 찾아옵니다. - 바닐라 스카이',
    '인생은 모두가 함께하는 여행이다. - About time',
    '당신은 지금, 언제나 그래 왔듯이 제 꿈속에 있습니다. - 노트북',
    '네가 원하는 것 무엇이든 말만 해, 내가 그것이 되어줄게 널 위해. - Notebook',
    '인생을 낭비하는 자 유죄. - 빠삐용',
    '제가 만약 오늘 죽는다면 제 삶이 아무것도 아닌 게 될까 봐 두려워요. - 소울',
    '나는 매 순간을 꽉 차게 느끼며 살아갈 거야. - Soul',
    '날 기억해 줘, 최선을 다해 우리는 할 수 있어. - 이터널 선샤인',
    '사랑 같은 건 없어, 그건 판타지야. - 500일의 썸머',
    '치열하게 살던가, 죽기만을 기다리던가. - 쇼생크 탈출',
    '자신의 존재는 잊어도 인생이 준 최고의 선물은 잊지 마. - 패밀리맨 (The family man)',
    '지금은 고백할래요, 내 희망사항을. 크리스마스잖아요. - 러브 액츄얼리 (Love Actually)',
    '우리 모두 어둠을 밝히려는 길 잃은 별들이 아닐까요? - 비긴 어게인',
    '네가 없는 곳은 기억나지 않아. - Eternal Sunshine of The Spotless Mind',
    '쓴맛을 못 느껴봤으면, 달콤한 것도 달콤한 게 아냐. - Vanilla Sky',
    '경험은 나이 들지 않아요, 경험은 결코 시대에 뒤떨어지지 않기 때문이죠. - Intern',
    '거 좀 힘들다고 울어 버릇하지 마, 어차피 내일도 힘들어. - 스물',
    '넌 더 이상 탓할 사람이 없어져 나를 욕했지만 나는 널 변함없이 사랑했어. - Begin again',
    '내일만 사는 놈은 오늘만 사는 놈한테 죽는다. - 아저씨',
    '인생은 미로 같고 사랑은 수수께끼 같죠. - 머니볼',
    '이제 눈을 뜨렴, 자 이제 좋은 세상이야. - The Blind Side',
    '난 과거의 너에겐 관심 없어, 난 현재의 너를 산거야. - Moneyball',
    '내 인생은 비극인 줄 알았는데 코미디였어. - 조커',
    '잊히지 않을 것 같은 무더운 여름 뒤엔 가을도 온다 분명히. - 500 Days of Summer',
    '내가 좋아하는 사람이 나를 좋아해 주는 건 기적이란다. - 어린 왕자',
    '역경을 이겨내고 핀 꽃이 가장 아름다운 꽃이다. - 뮬란',
    '내일은 내일의 해가 뜬다. - 바람과 함께 사라지다',
    '여기 보이는 건 껍데기에 지나지 않아, 가장 중요한 건 눈에 보이지 않지. - The little Prince',
    '우리가 두려워할 것은 두려움뿐이죠. - 주토피아',
    '변화는 너로부터 시작해. - Zootopia',
    '꿈은 도망가지 않아, 도망가는 것은 언제나 나 자신이야. - 짱구는 못 말려',
    '내 최고의 행운은 도박에서 이 배의 티켓을 딴 거야, 당신을 만났으니까. - 타이타닉',
    '삶의 종착역은 다 같아, 어떤 길로 가는지가 다를 뿐이지, 넌 네 길로 가는 거야. - 벤자민 버튼의 시간은 거꾸로 간다',
    '난 가고 싶은 곳에 가기 위해 뛰었는데 그게 삶의 기회가 될 줄 몰랐어요. - Forrest Gump']

  // 전체 영화 정보 저장목록
  const allMovies = ref([])

  const searchKeyword = ref('')

  const searchedMovies = computed(() => {
    if (searchKeyword.value) {
      // 검색 키워드가 있을 경우 필터링
      return allMovies.value.filter(movie => movie.title.includes(searchKeyword.value))
    } else {
      // 검색 키워드가 없을 경우 전체 목록 반환
      return allMovies.value
    }
  })

  const searchTheMovie = (movieKeyword) => {
    searchKeyword.value = movieKeyword
  }

  // 모든 영화 정보
  const initializeMovies = () => {
    getMoviesList()
      .then((response) => {
        if (response && response.data) {
          allMovies.value = response.data
          console.log('모든 영화를 불러왔습니다ㅎㅎ')
        }
      })
      .catch((error) => {
        console.error('Error getting all movies:', error)
      })
  }

  return { allMovies, searchedMovies, initializeMovies, searchTheMovie, loadingMessage }
})
