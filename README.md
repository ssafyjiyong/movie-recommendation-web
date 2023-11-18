# Movie Nomad
- 영화를 좋아하는 사람들을 위한 영화 추천 및 커뮤니티 서비스

# 프로젝트 목표
- 영화 데이터 기반 추천 서비스 구성
- 영화 추천 알고리즘 구성
- 커뮤니티 서비스 구성
- 서비스 관리 및 유지보수

# 개발환경
- Python 3.9.x
- Django 4.2.x
- Node.js LTS
- Vue.js 3.x

# 사용 API
- TMDB
- Spotify
- kofic(영화진흥위원회)

# Team M.A.D(Making A Difference)
pass

# 목표 서비스 구현 및 실제 구현 정도

# 데이터베이스 모델링 (ERD)

# 영화 추천 알고리즘에 대한 기술적 설명

# 서비스 대표 기능에 대한 설명

# 배포 서버 URL

# 후기

# 개발 노트
### 2023/11/16
- ERD 모델 구축

    ![ERD](ERD.jpeg)

- 컴포넌트 구조 설계

### 2023/11/17
- 장고에서 API를 사용하여 DB에 저장 구현

### 2023/11/18
- 중복으로 DB에 저장되는 문제 해결(검색 문자열 공백 제거)
- 영화 상세정보 조회시 빈 값들 업데이트 구현 및 ManyToManyField로 설정된 테이블 값 업데이트 해결
