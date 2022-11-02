# Synchronous & Asynchronous
- 동기식 : 순서를 가짐, 순서 외의 작업을 진행할 수 없다
- 비동기식 : 작업을 요청과 동시에 다른 작업을 진행할 수 있다
- 즉, 동기식은 요청이후 응답이 오지 않으면 진행이 불가능
- 비동기는 병렬처리 라고도 한다

## 비동기 사용 이유
- 사용자 경험 에 강점을 가지고 있다
- 로직 수행 중에 앱이 멈추는 것과 같은 현상이 발생
- 먼저 처리되는 부분을 보여줄 수 있기 때문에 사용자 경험에 긍정적인 결과를 가져올 수 있다

## Javascript 비동기 처리
- JS는 Single Thread로 한번에 하나의 일만 수행할 수 있다
- 하지만 어떻게 비동기로 처리할 수 있는 걸까?
### Javascript Runtime
- Runtime : 런타임은 특정 언어가 동작할 수 있는 환경
- 비동기와 관련된 부분은 외부 환경인 브라우저 또는 Node환경에서 처리 된다
- 비동기 동작 순서
  1. Call Stack : 우선, 모든 코드가 stack(LIFO) 에 들어가게 된다
  2. Web API : 만약 작업이 오래 걸리면 web API에서 별도 처리, 즉 JS는 따로 처리
  3. Task Queue : web api 에서 끝나면 Task Queue(FIFO) 로 따로 들어감
  4. Event Loop : call stack 이 모두 처리가 되면, task queue 의 문제들이 이제 처리됨 (참고로 task queue에서도 먼저 처리되면 먼저 callstack으로 이동)
- 추가 : 0 delay = 순서에 시간상 딜레이를 주지 않아도 비동기 과정으로 넘겨버릴 수 있도록 설정하는 것 / task queue로 넘어가므로 순서가 call stack의 최후미에 붙게 될 것이다

## Axios
- JS 의 HTTP 통신을 위한 라이브러리
- node에서는 npm, browser 은 CDN을 이용
- axios.method('url') .then(성공시 함수) .catch(실패시 함수)
- axios의 경우, 런타임으로 작동하게 되므로, task queue에 들어가게 된다
- axios는 이후 vue.js에서 django와의 통신을 담당하게 된다

## Callback Promise
- 비동기의 단점은 들어오는 순서가 아니라 작업이 완료되는 순서에 따라 처리된다는 것
- 즉, 실행 결과를 예상하면서 코드를 작성할 수 없게 함
- 콜백 함수를 사용함으로써 처리
### Callback 함수
- 다른 함수의 인자로 전달되는 함수
- 작업이 완료 후 실행할 작업을 명시하는데 활용할 수 있다
- 앞의 시점이 존재해서, 앞의 작업이 시행되면 => 콜백이 실행됨
- 즉, 비동기 처리를 순차적으로 동작되도록 만들 수 있다
#### 단점
- 연쇄적인 비동기 작업을 순차적으로 시행되게 만듦
- 콜백 지옥이라는 것에 빠져버린다 (무한 연쇄)
- Pyramid of doom 이라고도 불림
- 가독성을 해치고, 유지보수가 어려워짐

### Promise
- callback hell을 해결하기 위함
- Promise는 비동기 처리를 위한 객체이다, 즉 순서가 보장된다
- Axios 라이브러리가 이것의 활용하고 있다 (then, catch)
- then()
  - 요청한 작업이 성공하면 callback실행
  - 이전 작업의 성공결과를 인자로 받음
- catch()
  - 하나라도 실패시 실행
  - 실패 사유, 객체를 인자로 받음

- then, catch는 계속해서 chaining이 가능
- 깊어지지 않고 아래로 내려갈 수 있다 + 순서가 무조건 보장됨
- then 이 연속되려면 return으로 값이 반환되어야 한다
- 위의 모습과는 다르게 추천 표준 형식으로 작성하도록 하자
```javascript
const url = 'https://dog.ceo/api/brees/image/random'
const btn = document.querySelector('#dog-btn')
axios({
  method:"get",
  url : url,
  })
    .then((response) => {
      console.log(response)
      const imgsrc = response.data.message
      return imgsrc
    })
    .then((imgsrc) => {
      const imgTAg = document.createElement('img')
      imgTAg.setAttribute('src', imgsrc)
      document.body.appendChild(imgTAg)
    }) // chaining
    .catch((error) => {
      console.log(error)
    })
```
- axios 의 method에 따라 parameter가 다르다 -> 공식문서를 참고하자
- 