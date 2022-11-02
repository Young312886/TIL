# Vue CLI
- CLI = Command Line Interface
## Node.js
- 브라우저 밖에서 런타임 환경에서도 구동할 수 있게 해줌
- pip 대신 npm을 사용 / 의존성 패키지 관리자
## CLI 를 통한 서버 사이드 구축
- CLI 는 Vue 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
### 구조
- node_modules 
  - vue의 다양한 모듈들이 담겨있는 폴더
  - 상호 연관되어 있으므로 임의로 수정시 오류 발생 가능
  - gitignore을 통해 안올라가게 되어 있음
  - Babel
    - js의 컴파일러 역할을 함
    - ES6코드를 구버전으로 번역 / 변환 해줌
    - 코드 스펙트럼이 넓으므로 브라우저의 버전에 맞추어 대응이 가능하게 해주는 모듈
  - WebPack
    - static module bundler
    - 모듈간 의존성 문제를 해결
    - 모든 모듈 매핑과 내부 종속성 그래프 빌드
- package-lock.json
  - requirements 와 동일한 역할을 하는 친구
  - 협업 및 배포에 중요한 역할
  - npm으로 모듈 설치시, 알아서 업데이트 된다 (직접 수정 불필요)
- jsconfig / vue.config
  - 프로젝트가 진행되기 위한 config설정들
- public & src
  - 이후 작성할 내용들이 담기게 되는 폴더들

#### Module
- 개발 기능을 여러 파일로 분리하여 관리
- 각각의 파일 하나가 모듈이라 불리게 된다
- 클래스 하나 또는 복수 함수로 구성된 라이브러리 구성
- 모듈 관리 시스템 : ESM. AMD 등등
- 모듈 의존성 문제
  - 너무 많은 모듈들이 생기고, 상호 의존성이 깊어짐
  - WebPack은 이러한 의존성을 해결하기 위해 등장
  - 다시 모듈들을 묶어준다

### 구성 계속
- public
  - favicon = 아이콘
  - index.html
- src
  - src/assets 
    - static 파일들이 담기게 됨
  - components
    - 하위 컴포넌트들이 위치
  - app.vue
    - public.html과 연결됨
#### Component
- UI 를 독립적으로 재사용한 조각들로 나눈 것
- 기능별 코드 조각이다
- 다시 사용을 위한 소프트웨어 구성 요소
- 하나의 app에는 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적이다
- const app = new Vew() 로 선언하게 된 하나의 기능이 컴포넌트이다
- 또는 .vue파일 하나를 컴포넌트로 보기도 한다 = SFC(single file component)


## 데이터의 관리
- CLI 는 트리 구조를 가지고 있다
- 이러한 구조를 가지기 때문에 일정한 규칙에 의해 데이터 전달이 이뤄지게 된다
- 데이터 흐름을 파악하기 용이
### Props
- pass props
- 상위에서 하위로 데이터를 전달하기 위한 지정 특성
- props라는 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함
- 정적인 데이터를 전달하는 경우  static props라고도 함
- 반드시 캐밥 케이스로 작성 (html에서는)
- 이후 받는 거는 다시 camle case로 받음
- 우선 전달시, prop-data-name = 'value'
- 받을 곳에는, props : {propDataName : type} 로 타입 명시
- v-bind와 그냥 value값을 전달하는 것에서 약간의 차이가 발생
- v-bind는 javascript에서 변수를 찾아 그 변수의 값이 전달된다
- 그리고 모든 prop은 단방향 데이터 / 자식에서 수정시 오류가 발생

### Emit
- 자식에서 부모로 데이터가 전달
- 위의 html에서 action 할당
- methods에 함수 저장(안에 this.$emit('action name', 'values'))
- 변수 여러개 전달 가능
- 이후 @action-name:"ParentMehods"로 html에서 받고(v-bind형식)
- methods에서 정의해주기
