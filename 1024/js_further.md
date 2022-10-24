# Brower APIs
- 웹 브라우저에 내장된 API
- 현재 컴퓨터에 데이터 제공, 오디오 재생등 동적인 내용을 포함하고 있음
## 종류
- DOM
- Geolocation API (지리)
- WebGL (그래픽)

### DOM
- 문서 객체 모델 (Document Object Model)
- 구조화된 표현을 제공
  - 프로그래밍 언어가 DOM구조에 접근할 수 있도록 해줌
  - 스타일 변경, 내용 변경
  - 태그 추가, 스타일 추가
  - HTML과 CSS 조작 가능
- HTML 문서를 구조화하여 객체로 취급 가능
- DOM Tree
  - 문서를 논리 트리고 표현하게 된다
  - 프로그래밍 적으로 트리에 접근하고, 문서의 구조, 스타일 등을 변경할 수 있다
- 이러한 모습은 객체 지향적 표현이다
- 우리는 이러한 주요 객체들을 활용해서 접근하는 방법을 익혀야 한다

#### DOM 의 주요 객체
1. window
   1. DOM을 표현하는 창
   2. 가장 최상위 객체
   3. 탭 기능이 있는 브라우저에서는 각각의 탭을 의미한다
2. document
   1. 브라우저가 불러오 웹 페이지
   2. 페이지 컨텐츠 진입점 역할이며, 다른 요소를 포함하고 있음
   3. 윈도우의 하위 매체

#### 접근 방법
- querySelector
- querySelectorAll
- #id
- .클래스
- '> 하위 태그'
- NodeList
  - index로만 항목에 접근 가능
  - foreach 등 다양한 메서드 사용 가능
  - 다만, queryselector로 받은 것은 실시간 변화는 반영하기 어렵다
  - 실시간으로 변경하고 싶으면, childNodes와 같은 것을 활용하면 된다

#### Dom 조작
1. 생성
   - createElement(tagName)
   - tag의 html요소를 생성, 및 반환
2. 입력
   - innterText
   - 객체와 그 자손의 텍스트 컨텐츠를 표현
   - 줄바꿈 인식, 숨겨진 내용 무시 등
3. 추가
   - appendChild()
   - 특정 부모 node의 자식 nodelist의 마지막에 추가
   - 하나의 node만 추가, 및 반환
   - 만약 이미 존재한다면, 새로운 위치로 이동
4. 삭제
   - removeChild()
   - 제거 및 반환
5. 속성 조회 및 설정
   - getAttribute(attrName)
   - 요소에 지정된 값을 반환
   - 얻고자 하는 속성의 이름을 넣는다
   - setAttribute(name, value)
   - 지정된 요소의 값을 설정
   - 이미 존재하면 갱신, 없으면 추가
   - 참고로 클래스에 접근하는 방법은 classList를 접근하면 된다
   - h1Tag.classList.toggle('blue') 토글로 변환시키기

### Event
- 프로그래밍 하고 있는 시스템에서 일어나는 사건 또는 발생
- 특정 시점을 시스템이 알려주는 것
- 예로는 클릭을 통해 사건에 대한 결과, 조작을 할 수 있다
- 그 외에도 엄청 다양한 이벤트가 존재
#### Event Object
- Dom 에서 이벤트 수신 -> Event 처리 -> addEventListner() 를 html 요소에 부착
- EventTraget.addEventListner(type, listener)
- 대상 / 이벤트 / 할일 순으로 들어간다
- listener = call back function
- 참고로 listener함수의 인자는 유일하게 event 하나가 들어가게 된다
- 이벤트 취소
  - 이벤트가 발생하지 못하도록 막아버림(a태그나, 드래그 등)
  - addEventListener('copy', function (event) {event.preventDefault() alert('경고') })
  - copy라는 이벤트가 취소되게 만들어줌

### lodash
- 모듈성, 성능, 추가기능을 제공하는 js 유틸리티 라이브러리
- array, object등 간단한 유틸리티 함수들 제공

## this
- 어떠한 object를 가리키는 키워드
- js 에선 함수가 호출될 때 암묵적으로 전달받는다
- 하지만 다른 언어와는 다르게 동작한다
- 함수 호출 방식에 따라 this에 바인딩 되는 객체가 달라짐 (동적이다)
1. 전역에서의 this
   1. 전역 객체인 window를 의미함
   2. 밖에서는 global 과 같은 유일한 최상위 객체를 의미한다
2. 단순 함수 호출
   1. 전역 객체를 의미함
   2. window, global을 의미함
3. method 에서
   1. 객체의 메서드이므로 해당 객체를 불러오게 된다
   2. 이 경우, 해당 객체의 정보를 활용할 수 있게 된다
4. Nested 일 경우(callback 함수)
   1. 단순 호출 방식으로 활용되었으므로, 전역 객체인 window를 가리킴
5. nested에서 화살표 함수
   1. 위의 경우와는 다르게 안의 this 또한 해당 객체를 불러옴
   2. 화살표 함수에서 this는 자신을 감싼 정적 범위,
   3. 자동으로 한단계 상위 scope를 바인딩
   4. 화살표 함수는 약간 다르게 움직인다!!
- 다만, addEventListener 의 경우, 화살표 함수를 활용하면 this는 위의 객체인 전역을 가르키게 된다. 이 경우 기존에 활용하는 event.target을 불러오는 방식이 먹히지 않게 되므로, 그렇게 작성하면 안된다
- 