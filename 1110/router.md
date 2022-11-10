## UX / UI
- 사람들은 비슷한거 끼리 묶어주고 붙여주는 데 익숙함을 느끼게 된다
- 따라서 이러한 부분을 설계할때 고려해야 한다

### UX
- user experience
- 사용자의 경험에 따라 디자인 하는 것
- 이러한 부분을 데이터적으로 접근 하는 것도 하나의 방법
### UI
- 배치와 관련되어, 화면을 디자인 하는 것
- interface = 사용자가 기기를 동작시키는데 도움을 주는 시스템
- 좋은 ui는 이쁜 디자인 + 사용자의 편의

## 왜 라우팅인가?
- 동작에 따라 url이 반드시 변경되어야 한다
- 유저는 url의 변화로 페이지의 변경을 인식할 수 있다
- 또는 외부에서 바로 들어올 수 있다
- 그리고 뒤로 가기 사용 불가능

## vue Router
- spa 상에서 라우팅을 쉽게 개발 할 수 있는 기능 제공
- 페이지가 여러 페이지 인 거 처럼 보여주기\
- (MPA - multiple page application) / ssr 방식

## router 연결
```bash
vue add router
```
- history mode = 브라우저 history api를 활용하는 것 
- 새로고침 없이 이동 기록을 남길 수 있다
- router 안의 index를 통해 url을 mapping중
- 각각의 views를 통해 보여주고 싶은 페이지를 설정 가능
- 여러개의 페이지를 활용하는 거 처럼 보여줄 수 있음

### router-link 태그
- a태그와 동일한 모습
- 다만, 클릭 이벤트를 차단하여 다시 로드를 방지
- 목표 경로는 to속성으로 로드할 수 있게 해줌

### router-view 태그
- 이후 하단에 보여줄 페이지를 출력하는 구역
- 실제 component가 붙여질 자리
- block tag와 비슷
- 결국 app.vue는 장고의 base.html역할과 동일하게 됨

### router/index.js
- routes 를 통해 라우터들의 경로를 설정
- django 의 url.py와 동일

### src/views
- components와의 기능 차이는 별로 없다
- 단순 경로 차이를 부여하기 위한 것
- views의 파일들은 router들과 관련된 파일을, component는 그 외의 세부 파일들이 구성되게 된다

### 주소 이동 방식
- 선언정 방식 = router-link to='' 에 넣기
  - name 에 넣은 모습으로도 to에 넣을 수 있다 { name : '블라블라'}
- 프로그래밍 방식 = $router에 접근하는 방법
  - this.$router.push 사용
  - history stack에 새로운 url을 넣는 방식
  - methods에 click 이벤트 부여하고, this.$router.push({name : ''})방식
- 둘은 모두 같은 동작

### Dynamic Route Matching
- 장고의 variable routing
- path : 'hello/:userName'. component : () 

### lazy loading
- 당장 필요하지 않거나 초기 다운로드 속도가 너무 느린 경우
- 후에 다운로드 할 수 있도록 설정하는 것
- component: () => import('../vies/aboutView.vue')

### navigation guard
- vue router 로 특정 url을 접근 시 해당 접근을 막거나 redirect 하는 방법
- 전역 / 라우터 / 컴포넌트 3종류 
- 동작하는 구역에 따른 분류이다
#### 전역 가드
- global before guard
- 이동 시 항상 사용 됨
- router.beforeEach() 로 사용
- index 파일 하단 바로 위에 작성
```javascript
router.beforeEach((to, from, next) => {
  to 는 이동할 url정보 / from 은 현재 url정보 / next 는 지정할 url로 이동할 함수 (콜백함수 내부에서 한번 호츨, to로 이동할 것임)
})
```
- next 호출 하지 않으면 화면 대기 상태에 빠짐
- 여기서는 login 여부를 확인해 보도록 하겠다
```javascript
router.beforeEach((to, from, next) => {
  const isLoggedin = true // 이후는 서버에 조회할 것이다
  // 로그인이 필요한 페이지 목록
  const authPages = ['hello']
  // 움직일 페이지가 로그인을 요하는가?
  const isAuthrequired = authPages.includes(to.name)
  if (isAuthrequired && !(isloggedin)) {
    next({name : 'login'})
  } else {
    next ()
  }
})
```
- 위와 같이 설정이 맞으면 로그인, 아니면 기존으로 이동하도록 설정

#### 라우터 가드
- 특정 라우터에만 적용
- beforeEnter()
- 라우터 등록한 위치에 추가해주며, 다른 경로에서 탐색할 시에만 적용
```javascript
const loggin = true // 로그인 조건 찾아서 저장
// {path : '/login  안에 넣어주기'}
{
  beforeEnter(to, from, next) {
    if (loggin) {
      next({ name : 'home'})
    } else {
      next()
    }
  }
}
```
- 로그인 되면 home페이지로 이동하도록 설정

#### 컴포넌트 가드
- 특정 컴포넌트 안에서 가드 지정
- beforeRouteUpdate()
- 컴포넌트가 재사용되는 경우, 컴포넌트는 변화하지 않지만 url이 변화하는 현상 발생 가능
- 이를 방지하기위해, 위의 방식 활용
- 해당 컴포넌트 내에 함수 작성
```javascript
beforeRouteUpdate(to, from, next) {
  this.userName = to.params.userName
  next()
}
```
- 위의 방식으로 url params의 변화를 감지하여 다시 컴포넌트에 적용시켜주는 것이다

##### 응용 (404 not found)
- 없는 모든 경로를 404로 
  - path: "*", redirect: '/404'
- 등록은 되었는데 이상한 곳으로 요청하는 경우(형식만 유효할 시)
  
articles with vue