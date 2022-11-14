# vue
## Vue with DRF 
- DRF를 통해 data를 vue로 전달
- Server = DRF / Client = Vue

### Ajax 요청
- 현재 과정에선 vuex를 활용하여 비동기 작업을 진행할 것이므로 vuex에서 통일하여 작업
- axios api_url 을 django url로 기본 설정
- 이 작업 시작 전, vuex 호출하는 것 component에 작성
  
### SOR & CORS
#### SOR 
- 기본적인 보안상 정책으로 인해 브라우저는 같은 출처(origin)의 데이터만을 받아들이게 작동하고 있다
- 토큰과 쿠키와 같은 보안 정책이 외부 브라우저로 이동하면서 해커의 위협에 노출될 수 있는 상황을 막기 위함
- host, port, protocol 모두 동일해야 동일한 출처라고 판단하게 된다
- 현재, vue와 django간의 통신은 port가 동일하지 않아 발생하게 된다

#### CORS (Cross Origin Resource Sharing)
- 이러한 출처가 다른 두 서버간의 교차를 위해선 CORS 정책을 따라야 한다
- 기본 보안 정책을 담당하며, 2가지 오청방식이 존재한다
- 우선은, Simple request로 진행하겠다
- header를 활용, 외부 브라우저에서 해당 접근 권한을 부여하도록 하자
- 해당 클라이언트를 인증할 수 있도록 서버에 지정하는 방법이다
- django-cors-heards 등록(github참고)