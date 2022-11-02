# Web App
- 웹 페이지가 그대로가 아닌 디바이스의 App처럼 보이는 것
- 적절한 사이즈의 UX/UI의 형태로 표현된다

## SPA
- 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
- CSR(Client Side Rendering)방식으로 처리하게 된다
- SSR이란?
  - 기존의 요청방식
  - 서버가 html을 렌더링 하여 제공한다
  - client는 단순히 전달받게 된다
- CSR이란?
  - 한장의 html을 서버로부터 수신
  - 내용 자체는 자바스크립트가 스스로 그리게 된다
  - AJAX로 요청 => Json데이터 수신 => JavaScript로 데이터 처리, DOM트리에 반영(렌더링)
- CSR 장점
  - 모든 html을 서버로부터 수신하지 않아도 됨 = 속도 향상과 트래픽 감소
  - 매번 모든 부분을 수정이 아닌 부분 수정 가능 = UX 향상
  - 백과 프런트의 구분이 명확해짐
- CSR 단점
  1. 첫 구동의 데이터 양에 따라 최초 작동 시간이 느려질 수 있음
  2. 검색 엔진의 최적화가 어려움 (html자체에는 아무것도 없기 때문)
- 점차 두 방식 모두를 지원하는 framework가 발전하고 있다

# Vue
## 장점
- 간단, 가볍
- 확장성도 좋다
- 다른 코드 이해하는 입문으로 최고다

```javascript
const vm = new Vue({
  el: '#app',
  // el = element, 원하는 태그나 영역을 선택하는 과정, 그 안에있는 친구들만 영향을 받게 됨(마운트 된다)
  // html 상의 { {} } 부분은 출력 부분(interpolation)으로 할당하는 data가 출력되게 됨
  data : {
    message : 'hello',
  },
  // 또한 데이터는 객체로 구현해주어야 한다, 추가로 this로 접근가능해야 한다
  methods : {
    // Vue가 this가 됨
    // 각각의 메서드들은 변수 이름인 app.print()형식으로 호출 할 수 있다
    print : function () {
      console.log(this.message)
    },
    bye : function() {
      this.message = 'Bye'
    },
    // 참고로 method 선언 시 arrow 함수를 사용해서는 안됨. 그 경우 this가 꼬이게 되서 오류가 날 수 있다 (이 경우 this는 window를 가르키게 됨)
    
  }

})
```
## 문법
- data안에는 우선적으로 문자열이 반영되게 되어 있음
- 다만, v-html 속성 ( = rawHTML)을 tag안에 부여한다면, html형식이라면 알아서 해석하여 속성을 부여 가능
- interpolation 안에는 js의 표현식을 넣을 수 도 있다

### Directives (v-name)
- v-접두사가 있는 특숫 속성에는 값을 할당할 수 있음
- 표현식의 값이 변경될 때 변화값을 반영할 수 있음
- 접두사와 뒤에 : 과 . 에 붙는 다양한 변수에 다양한 역할을 함
1. v-text
   1. { { } }과 유사한 역할
   2. 가장 기본적인 바인딩 방법
2. v-html
   1. raw html을 표현할 수 있다
   2. 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지(해킹 가능)
3. v-show
   1. 표현식의 boolean값에 따라 뒤의 값을 렌더링 할지 안할지 결정
   2. display 속성값을 toggle하는 것이다 = 코드는 존재
4. v-if
   1. v-show 와 동일
   2. 하지만 값이 false면 html내에 존재하지 않음
   3. else, ifelse 등 다 된다
- show 와 if간의 차이는 initial load 와 toggle 간의 비용이 다르다
5. v-for
   1. for...in...형식
   2. 반복할수 있는 모든 데이터 형식에 사용 가능
   3. 인덱스를 동시에 받으려면 (char, index) 형식으로 받자
   4. 안의 객체에 대해서도 접근 가능
   5. key 는 특수 속성 : v-for를 사용시 반드시 할당해 줄 것. 고유값으로 순환의 기준이 됨
6. v-on
   1. :이후의 인자를 확인 (event)
   2. 값으로 js표현식 작성
   3. addEventListener와 동일한 인자와 값으로 구성
   4. @로 v-on 대체 가능(대부분 그렇게 함)
   5. 인자 또한 파라미터로 ()안에 삽입 가능
7. v-bind
   1. vue.data의 변화에 반응하여 dom에 상황에 따라 유동적 할당 가능
   2. 속성값을 변수로 할당 가능
   3. :shortcut 제공(대부분 이걸로 작성)
   4. {}를 통해 toggle 가능
   5. 배열을 통해 여러 값을 부여 가능
8. v-model
   1. 하나의 문자가 온전히 입력되면 변화가 반영됨
   2. 양방향 바인딩이 발생
   3. 다만, 한중일의 경우 불가능
#### advanced
- instance 가 가진 option들
  1. computed
     1. computed 는 계산된 값 (method와는 다름)
     2. 한번 호출하면 일정 값만을 말함
     3. 