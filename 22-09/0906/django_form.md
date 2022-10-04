## Django form
- 데이터 베이스는 요청을 모두 수용한다
- 이러한 들어오는 데이터가 원하는 형식인지 확인하는 유효성 검증이 필요
- Django form  은 이러한 유효성 검증을 쉽게 진행할 수 있도록 도와준다
- *단순화 및 자동화* 에 연관되어진다

### 처리 과정
1. 렌더링
2. foms 생성
3. 데이터 수신 및 처리

## Django Form Class
- Form 관리의 핵심
- Model 선언과 유사
- 다만, 일치하지는 않는다
- 참고로 forms.py 위치는 자유자재로, 이름도 규약이 되지 않지만 가능한 일정하게 작성하자
- 기존에 input 과 form 태그로 작성한 부분을 전체 form class로 대체해버릴 수 있다
- 다만, 기본에는 띄어쓰기가 없다는 점, 줄바꿈이 없다는 점, textarea가 막상 존재하지 않는 다는 점
### options
1. as_p - p태그로 감싸기
2. as_ul - li태그로 감싸짐 (ul은 직접 쓰면 됨)
3.  as_table - tr행으로 감싸짐

### Widget
- 기존의 없는 표현들을 추가시키는 것
- 요소 렌더링을 담당
- 즉, 단순 출력 부분을 담당, 유효성 검증과는 관련 없음
- form fields에 할당됨
## ModelForm
- model과 form 간의 중복되는 부분이 많다는 점에서 착안
- 결국 너무나도 많은 양의 코드를 작성해야 한다는 것이다
- model을 기반으로 한 form을 작성해보도록 하자
- 즉, 재정의 불필요함이 감소
- model과 form의 정보가 매우매우 밀접하게 연관되어 버림
- meta 안에 model / fields를 할당해야지 그러하게 움직이게 된다!!!
- exclude 를 작성하면 전체에서 빠질 놈들만 할당 가능
- class 이름이 Meta인 이유는 meat데이터임을 할당해주는 것이다
- model안에 참조값을 작성한다. (호출이 아닌)
  - 참조값을 활용하는 경우는 인스턴스를 활용이 아닌 이후에 필요한 시점에 활용하기 위함이다
  - 내부 속성, 필드 등을 참조하기 위함
- is_valid()
  - 유효성 검사의 메소드
  - 모든것이 여기에서 이뤄진다.
  - 정답이면 Return = True
  - 아니면 객체.errors 가 추가로 생성되어서 반환된다

### Widget 추가
- 이후 form 클래스 안에 자유롭게 html의 속성들을 attr안에 추가할 수 있다.
- 이러한 과정을 통해 손쉽게 원하는 스타일의 form태그 구현 가능

## HTTP Request
- request 처리를 위한 view함수 변화
- new-creat / edit-update 간의 공통 로직 존재
- 메서드 간에 처리를 분리해서 한번에 처리 가능
- 따라서 앞선 시간에 작성한 기능에 따라 분리된 함수가 통일된 하나의 함수로 작성될 수 있다.

### allowed 함수
아래의 함수들을 통해 get과 post 메서드 사용에 대해 제한, 또는 확정을 지을 수 있다
이외에는 405오류를 반환하도록 설정하는
1. require_safe()
    - requires_get()이 있지만 safe를 사용하자
    - get만 허용
2. require_http_methods
    - get, post둘다 허용 가능
3. require_POST
    - post만 허용


## authentication system(인증)

