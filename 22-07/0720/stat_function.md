### 제어문
특정 상황에 따라 코드가 실행되거나(조건/분기) 반복 실행되는 제어의 역할을 함
#### 조건문 
참 / 거짓을 판단하는 조건식을 활용

** if / elif / else **

* 조건식을 한줄로 표현 : 삼항연산자
* 단, 참 if 조건식 else 거짓 형식만 가능(elif는 else뒤에 if 조건문을 한번 더 넣자)
 
#### 반복문
특정 조건을 만족할때까지 같은 동작 반복
** while for + break continue for-else

* while은 조건 만족 전까지 계속 반복 => 탈출 조건을 반드시 잘 작성해야 한다
* for문은 순회 가능한 객체를 요소로 순환 => 별도의 탈출이 필요하지는 않음
    * iterable 순회가 가능한 (순서O)

### 함수
축약(abstraction)을 위한, 재사용성과 가독성, 생산성을 높이기 위한 코드 작성을 위해 함수를 사용하자

종류
+ 내장함수 - 기본함수
+ 외장함수 - import를 통한 라이브러리 함수
+ 사용자 정의 함수 - 내가 만드는 함수

#### 기본 구조
* 선언과 호출 (define & call)
* 입력(input)
* 문서화 (Docstring)
* 범위(Scope)
* 결과값 (output)

특이 사항
+ return 을 만나게 되면 함수가 종료 
+ return이 없다면 반환하는 값이 없음
+ print 는 return이 아님을 반드시 알자

+ Prameter 는 정의때의 변수 / Argument 는 호출시 넣는 값
  + 함수의 Argument는 기본적으로 Positional로 들어간다
  + 하지만 x = x, y = y 처럼 keyword argument 가능
  + 단, keyword 다음에 positional은 불가능
  + parameter 설정 시 default argument 설정 가능

+ 가변인자(*) (튜플로 처리)
  + 몇개의 Positional argument를 받아야 할지 모르는 상황에서 활용
  + *를 활용하면 언패킹시 남는 변수를 리스트에 담아둘 수 있음 (원래는 오류 발생함)
  + 추가로 가변인자의 경우 추가적인 인자로 인식 가능 (옵션, 없어도 무방)

+ 가변 키워드 인자 (**)
  + 딕셔너리로 묶여 처리
  + 받은 변수안에 keyword arguments가 들어오게 되고, 이를 딕셔너리 형태로 저장시켜줌

+ Scope (local/global)
  + global 은 어디서든
  + local은 함수의 scope 안에서
    + 변수의 수명 주기(name space가 기준이 된다)
      + built-in 은 실행 이후부터 
      + global은 인터프리터 종료 전까지
      + local은 함수 종료 전까지
      +  * name space 순서 = local < enclosed < global < built-in 
 + Global
   + 이러한 변수의 전역으로 선언하기 위해선 global 변수 형식으로 설정, 함수 안과 밖에서 변화된 값이 이후에도 사용될 수 있다.
   + Parameter값에 global 사용 불가능
   + global 선언 이전에 변수 사용 불가능
 + nonlocal
   + enclosed scope 에서의 변수 활용 여부 설정
   + 다만 global에는 영향을 주지 않음
   + 또한 이미 할당된, 선언된 변수에다가만 활용 가능

+ 다양한 함수
  + filter / zip / map / lambda
  + 재귀 함수
    + 자기 자신을 참조하는 함수
    + 함수 내에 자기 자신을 다시 호출
    + 다만, 재귀 깊이(or 횟수)가 최대 1000번(기본값)

#### 모듈과 패키지
+ 다양한 모듈을 하나로 = 패키지
+ 다양한 패키지를 하나로 = 라이브러리

* 모듈과 패키지 만들기
* 파일 구조
  * __init__.py (이전에는 필수지만, 지금은 자연스럽게 인식 가능)
  * check.py