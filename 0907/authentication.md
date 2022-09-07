## Authentication
- 인증과 권한 시스템
- 필수 구성은 settings.py에 이미 포함되어 있다
- Authentication & Authorization
### Custom User Model
- 기본 user model을 필수적으로 custom로 대체 해야 한다
- 기본 model에서는 username 을 식별값으로 사용 중
- 게다가 auth user model의 경우 migration이후에 수정이 매우 매우 힘듬
- 따라서 초기 설정시기에 변경시켜주어야 한다
#### Custom user model replace
- 공식 문서에 소개중
- 1. class user 작성 (AbstractUser 상속)
- 2. AUTH_USER_MODEL = 'accounts.User
- 3. admin.py 에 custom user model 등록 / admin.site.register(user, useradmin)
##### AbstactUser
- user model구현하는 추상 기본 클래스 이다
- 추상 기본 클래스란?
  - 공통 정보를 모델에 넣을 때 사용하는 클래스
  - 이 클래스는 테이블로 생성되지는 않는다
  - 대신 다른 모델의 기본 클래스로 사용되면 필드 추가의 역할을 한다
#### Database Reset
- 기존의 migrate 된 파일들의 경우 custom user model의 적용을 위해선 초기화 시키고 진행시켜야 한다
- migrations 안의 파일 삭제(__init__ 제외)
- db 파일 삭제
- 이후 재 migration
### Cookie
#### HTTP
- Hyper Text Transfer Protocol
- 리소스를 가져올 수 있게 해주는 프로토콜
- 특징
  - 비연결 지향
  - 요청 이후에는 연결이 끊김
  - 무상태
  - 연결이 끊기면 상태 정보가 유지되지 않음
  - 완전 독립적이다
- 그럼 로그인 상태를 유지시켜 주는 것은? "쿠키"
#### 쿠키
- 상태가 있는 세션을 만도록 해줌
- 상태를 유지시켜 주는 쿠기 = 세션
- 사용자 기록 정보 파일
- key-value형식으로 브라우저에 저장
- 이후 서버에 재요청시 저장된 쿠기를 전송 (매번)
- 이러한 쿠키를 동일 브라우저에서 왔는지 판단
- 즉, 로그인 상태를 유지할 수 있게 된다
##### 쿠키 사용 목적
1. 세션 관리 - 로그인, 팝업, 장바구니 등
2. 개인화 - 사용자 테마, 선호 설정
3. 트래킹 - 사용자 행동 분석
##### 세션
- 상태를 유지시키는 쿠키
- session id 를 발급 후 쿠키에 저장
- 이러한 session id 만이 전달되고, 이 id를 바탕으로 홈페이지가 전달됨
- 세션이 종료되면, 브라우저가 종료되면 삭제됨

### Login
- session create
- AuthenticationForm 
  - 로그인을 위한 built-in form
  - username & password 받음
- login(request, user, backend = None)
- 인증된 사용자를 로그인 시키는 로직
- 세션에 데이터를 입력하는 과정 
- get_user() 는 유효성 이후 로그인 사용자 객체 반환

### Logout
- session을 삭제
- httprequest를 인자로 받음, 반환값 없음!!!
- 1. session data db에서 삭제
- 2. 쿠키에서도 session id 삭제
- 위의 두 곳에서 삭제를 통해 다른사람의 접근을 막기 위함

### 회원가입
- User 를 create하는 것이다
- 다만, 권한이 없는(일반) 유저를 생성하는 것이다
- 3가지 필드를 가짐
  - Username
  - PW1
  - PW2

### Custom vs Base
- There could be some collisions happen after we declair custom user
- 다시 작성하거나 확장해야 하는 것
  - UserCreationForm
  - UserChangeForm
- class Meta 안의 User를 커스텀 해 줘야 한다

### 회원 탈퇴
- User 를 delete
- 기본적인 것은 동일하다