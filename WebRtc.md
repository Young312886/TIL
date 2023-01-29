# WebRtc
## 웹 소캣
- 양방향 통신
- 실시간 네트워킹
- 모두 가능하게 하는 방법
- https 프로토콜을 활용해서 한다
- 반드시 get, 사용
- handshake를 통해 http 가 업그레이드 되고, client간의 직접적인 통신이 시작된다
- 이후 쌍방향으로 통신이 이뤄지고, 한쪽이 끊는다면 즉시 연결이 끊기게 된다
- 이것은 최초에 메시지 형태만을 주고 받는데에 익숙하였고, 이후 STOMP와 같은 형식을 서브프로토콜로 자주 쓰게 되었다

## WebRTC
- Web Real Time Communication
### 각 서버들의 역할
- Signaling Server 
  - 가장 기본 서버
  - Peer 를 연결하기 위한 서버
  - 앞서 말한 handshaking 이 이뤄지는 곳이다
  - Client - Sever 간의 통신은 websocket을 통해 이뤄진다
- Stun Server
  - 방화벽이 있기 때문에 Peer간의 직접적인 통신이 불가능하다
  - 이때 Turn과 Stun이 활용된다
  - Stun은 자신의 IP를 알려주는 서버
  - 이미 있는 서버를 활용하자 (무료)
- Turn Server
  - 보호정책이 더욱 강한 NAT나 라우터의 경우 이를 우회해야 한다
  - 이 경우 우회하는 서버인 Turn을 활용한다
  - 이 경우 P2P는 아니게 된다
  - 즉, 최후의 수단

## 채팅 기능
참고자료[https://velog.io/@cksal5911/WebSoket-stompJSReact-%EC%B1%84%ED%8C%85-1]
- npm i soketjs-client, @stomp/stompjs --save
- 위를 통해 socket.js 를 인스톨해주자
```javascript
import SockJS from 'sockjs-client';
import StompJs from '@stomp/stompjs';

const client = new StompJs.Client({
  brokerURL: '/api/ws',
  connectHeaders: {
    login: 'user',
    passcode: 'password',
  },
  debug: function (str) {
    console.log(str);
  },
  reconnectDelay: 5000, //자동 재 연결
  heartbeatIncoming: 4000,
  heartbeatOutgoing: 4000,
});

// 연결 및 에러 처리 함수
client.onConnect = function (frame) {
    // 연결되면
};

client.onStompError = function (frame) {
    // 오류나면
  console.log('Broker reported error: ' + frame.headers['message']);
  console.log('Additional details: ' + frame.body);
};
client.activate();
client.deactivate();
// 소켓 미지원 브라우저 일시 (여기는 추가)

if (typeof WebSocket !== 'function') {
  client.webSocketFactory = function () {
    return new SockJS('http://localhost:15674/stomp');
  };
}
```

- 위의 코드를 활용하여 소켓간의 통신이 일단 구축됨
```javascript
const binaryData = generateBinaryData();
client.publish({
  destination: '/topic/special',
  binaryBody: binaryData,
  headers: { 'content-type': 'application/octet-stream' },
});
```

## 하지만
- 결론적으로 socket 보다는 webrtc를 더 자주 사용한다
- 이유는 webrtc 는 영상과 임의의 데이터 통신을 위해 셜계 되어 있어서
- 더욱 빠르고 지연시간도 짧다
- 즉, 고성능

### 참고용
참고용 Github[https://github.com/thms200/peer-client]
Openvidu Error [https://velog.io/@kimyunbin/Openvidu-%EC%BB%A4%EC%8A%A4%ED%84%B0%EB%A7%88%EC%9D%B4%EC%A7%95-%ED%95%98%EA%B8%B0]

와 그냥 webrtc [https://velog.io/@ehdrms2034/WebRTC-%EC%9B%B9%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EB%A1%9C-%ED%99%94%EC%83%81-%EC%B1%84%ED%8C%85%EC%9D%84-%EB%A7%8C%EB%93%A4-%EC%88%98-%EC%9E%88%EB%8B%A4%EA%B3%A0]
