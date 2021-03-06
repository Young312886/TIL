## 파이썬 기초 학습
---

#### 프로그램이란? 
특정 작업을 수행하는 일련의 명령어들의 모음

즉, 컴퓨터가 해야하는 일이 적혀 있는 것
  (소프트웨어 또한 유사한 의미로 종종 사용 됨)

##### 프로그래밍?
프로그램을 만드는 행위
  (코딩 또한 유사 의미로 사용됨)

##### 프로그래밍 언어
컴퓨터와 사람이 소통하기 위한 언어 표현 방법

컴퓨터의 기계어의 대안 이다

사람이 이해할 수 있는 문자로 구성 

기본적인 규칙과 문법이 존재

사람이 작성 = 소스코드
기계어로 번역(interpreter, compiler) = 기계어


#### 기초 문법
그전에 짚고 넘어가야 할 것
스타일 가이드에 맞춰서 작성하도록
들여쓰기 혼용 금지
적절한 주석의 작성은 좋다

##### 변수
데이터를 담는 상자

##### 연산자
"+ - * / // % **"
연산자 우선순위 존재(수학의 순서와 동일, 계산 이후에 논리 연산자 작동)

##### 자료형 분류
Boolean / Numeric(int, float, complex) / String / Nan

** 부동 소수점
실수 연산시 2진법 환산시 정확하게 표현이 안되는 경우가 발생

매우 작은 수 보다 작인지를 확인 하거나 (a-b) <= 1e-10 (엡실론을 활용)

math모듈 활용 math.isclose(a,b)

##### 문자열
escape sequence
\n : 줄바꿈
\t : 탭
\r : 캐리지 리턴 (커서를 맨 앞으로)
\0 : NULL
\ \ : \
\' : (')
\" : (")

문자열 또한 연산이 가능하다
덧셈, 곱셈 가능

String Interpolation (문자열 안에 변수 작성)

1. %-formating
   "   %s" % 변수
2. str.format()
   '   {}' .format(변수)
3. f-string
   f'   {변수}'

##### Boolean
True & False
(1,0)

참고로 일부 0값은 가끔 false로 취급 된다 (=falsy)
이러한 값들은 bool()안에 넣어서 확인해보자
##### 논리연산자
NOT AND OR 


##### Container
LIst에 관하여

##### Set 
set()
중복 불가 / 순서 존재 안함 (집합)

##### Dictionary
{key:value}

##### 하고 나서 느낀점
음 매일 하는 homework하고 workshop은 반드시 해야겠다

그리고 작성하는 내용 자체도 참고해야 하는 용어라든지 이러한 측면에 관하여 좀 자세하게 적어서 공부해둬야 겠다.