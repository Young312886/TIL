## CSS
### CSS layout techinques

#### Float
- css 레이아웃 중 하나
- 기본적인 박스와 inline구조(normal flos)에서 벗어나 wrapping하도록 만듦
- 다만 일부만 설정해 주면 기본 배치와 겹치게 되어 버린다 (감싼다가 기본이기에 설정된게 아닌걸 감싸게 된다)
#### Fleible box layout
- 행과 열 형태로 아이템을 배치하는 1차원 레이아웃
- flex를 사용하면 block이 inline처럼 변화가 됨
- Main axis와 cross axis가 존재
- 각각의 방향에 따라 순서와 회전 방향이 결정됨
- Flex container = 부모요소 Flex item = 자식 요소
- 속성들
  - 배치설정
    - flex-direction (main axis방향)
    - flex-wrap : container 안에 들어오도록 (자동 줄바꿈 / 기존 사이즈 유지)
  - 공간 분리
    - justify-content(main axis) : 컨테이너 안의 어디에 위치할 것인가 or 사이 간격을 어떻게 설정할 것인가 (space-around, evenly)
    - align-content (cross axis) : cross 기준 어디에 배치
  - 정렬
    - align-items (cross 기준으로) : cross 기준 위아래나 확장 느낌 (baseline = 글자 아랫선을 맞추기)
    - aligh-self (개별로) : 개별로 상자 내 위치 정렬 
  - 기타
    - flex-grow : 남은 영역을 아이템에 분배
    - order : 배치 순서 (개별로 설정 가능)

## BootStrap
- Quickly / Responsive grid system / Popular 의 키워드로 설명 가능
- CDN 을 활용해서 쉽게 부트스트랩을 다운받지 않고도 활용 가능하다(외부 서버 사용으로 부하가 적어짐)
- 모든 디자인을 html의 class값으로 쉽게 넣을 수 있다
- 이후 <script src = "url"></script> 안에 넣어준다
### BootStrap 활용
1. Spacing (Margins & Padding)
   - {property}{sides} - {size} 형식
   - property = margin(m) / padding(p)
   - sides = t / b / s / e / x(left,right) / y (top,bottom)
   - size = 0,4,8,16,24,48 순으로 증가(1size당) (auto도 들어감)
#### 반응형 웹
- 그리드 시스템과 breakPoing를 활용해서 구현
#### Grid System
- Column : 컨텐츠 부분
- Gutter : 칼럼간의 사이 공간
- Container : 칼럼들을 담는 공간
  - 12개의 Column / 6개의 Grid Breakpoints 
  - 