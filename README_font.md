## Front-end

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


