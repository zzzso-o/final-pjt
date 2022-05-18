# 2020 Movie Website Project

> SSAFY 1학기 최종 프로젝트로 영화 추천 사이트를 구현하는 과정을 README로 작성한다.

---

[TOC]

---

## Project Period
2020.11.19 - 2020.11.27

## Contributors
- 이송영 (팀장)
- 이민정

## :exclamation: 시작 전 CHECK_LIST

### :ballot_box_with_check: pip 설치

> 프로젝트에 필요한 pip를 설치한다. 

- `final-pjt-server/requirements.txt` 파일을 참조한다.

### :ballot_box_with_check: npm 설치

- npm 사용을 위해서 `node.js`와 `Vue Cli`가 설치되어 있는지 확인한다.
- `final-pjt-client` 폴더 안에서 아래의 명령어를 실행해본다.

```bash
$ node -v
```

```bash
$ vue --version
```

- 이후 아래의 npm을 설치한다.

```bash
$ npm install
```

- 기본 Vue 프로젝트 생성 이후, 추가적으로 설치한 npm은 아래와 같다.

```bash
$ npm install axios
$ npm install lodash
$ npm install vue bootstrap-vue bootstrap
```

- vue bootstrap 설치 후, 해당 패키지를 등록한다. 자세한 내용은 [공식홈페이지](https://bootstrap-vue.org/docs)를 참조한다.

```markdown
 # vue bootstrap 사용예시

<template>
  <div id="app">
    <b-button>Button</b-button>
    <b-button variant="danger">Button</b-button>
    <b-button variant="success">Button</b-button>
    <b-button variant="outline-primary">Button</b-button>
  </div>
</template>
```

### :ballot_box_with_check: API 키 관리

- 프로젝트의 영화 데이터를 수집하는 API의 url과 key는 `final-pjt-server/movies/get_movie_data/api_key.py`에서 관리한다.
- gitignore로 관리되기 때문에 데이터 수집을 위해서는 해당 폴더에서 새로운 `api_key.py`를 작성하여 사용할 수 있도록 한다.
- `api_key.py`의 코드는 다음과 같다.

```python
# api_key.py

class URLMaker:
    url = 'https://api.themoviedb.org/3/movie/popular'
    key = '<API 키 값>'

    def __init__(self, key):
        self.key = key
        self.url = url
```

### :ballot_box_with_check: .env.local

> Vue 클라이언트 프로젝트의 최상위 폴더에는 `.env.local` 파일이 작성되어 있으며, 이것은 gitignore로 관리되어 있기 때문에 반드시 해당 파일을 생성하고 프로젝트를 진행하도록 한다.

- `.env.local` 파일에는 다음과 같은 데이터가 저장되어 있다.
  - `서버 url`

```
VUE_APP_SERVER_URL=http://127.0.0.1:8000
```



## 1 .팀원 정보 및 업무 분담 내역

### 팀장 : 이송영

- **Vue 클라이언트 구현**
- front-end

### 팀원 : 이민정

- **DRS 서버 로직 구현**
- back-end

