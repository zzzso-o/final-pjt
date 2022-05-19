## Front-end

```
VUE_APP_SERVER_URL=http://127.0.0.1:8000
```

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

### 
```bash
vure create final-pjt-front
```
프로젝트 위치에 맞춰서 npm install및 create project를 해줘야함 
npm vuex 설치시 
code ERESOLVE, ERESOLVE unable to resolve dependency tree 에러가 발생해서
npm i vuex --legacy-peer-deps 통해 vuex를 설치해주었다. 
vue add vuex
npm i vue-router 설치에도 같은 오류가 빌생해서 --legacy-peer-deps를 붙여주어서 해결하였다. 
npm i axios
npm i lodash
npm i buefy # UI Component for vue.js based on Bulma

router 설치하려고했더니 
96 packages are looking for funding
  run `npm fund` for details
이라고 말하면서 돈낼 수 있는 링크를 보여줬다.
npm config set fund false --global 을 통해서 fund기능을 꺼주고 다시 
npm i vue-router --legacy-peer-deps
npm add router 
그리고 history mode를 사용하기로함

vue cli 버전이 
$ vue cli --version
@vue/cli 5.0.4 였음
그래서 npm install -g @vue/cli@3.0.1 을통해서 3 버전으로 다운그레이드
=> 아무 소용 없었음

npm install vuex@2.0.0
뷰를 대충 위에서 아무버전이나 설치한게 문제였던걸까..


-------------------------


영화 진흥위원회에서 일별 박스오피스를 받아오려고 했는데
오늘 날짜로는 아무것도 안나오고 어제꺼부터 나와서 하루전걸로 해야함

```javascript
const today = new Date()
const yesterday = new Date(today.setDate(today.getDate() -1)).toISOString().split("T")[0]
const DATE = yesterday.replaceAll('-',"") 
```
위에서부터 오늘날짜 어제날짜 형변환 , 대시 없애주기 

-----------------------

CORS이슈를 해결하기 위해서 설치 
npm install http-proxy-middleware --save
=> vue.config.js에서 proxy설정을 해주었는데
잘 안되어서 검색 api는 스킵..

node-v 
node.js 버전이 16.15
그래서 corepack enable 
npm install --save cors로 
node.js의 미들웨어 CORS를 추가해주었다.
그리고 yarn add cors

--------------------


영화 진흥위원회에서 가져온 주간 박스오피스가.. poster url이 없어서
tmdb get latest로 변경
=> latest movie가 존재하지 않아서 계속 404 not found가 발생함
=> now_playing으로 변경 