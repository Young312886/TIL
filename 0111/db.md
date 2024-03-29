# DB 설계의 목적 

- 프로젝트, 명세서 등의 정보 요구사항에 대한 정확한 이해
- 분석자, 개발자, 사용자간의 원활한 의사소통 수단
- 데이터 중심의 분석 방법
- 현행 시스템만이 아닌 신규 시스템 개발의 기초 제공
  - → 설계를 “대충”하면 기능 한 개 추가 될 때마다 DB와 관련된 이미 개발된 프로그램도 함께 뜯어고쳐야 하는 경우가 있다.  → 설계를 꼼꼼히 하자!

1. 설계를 위한 요구사항 분석
- 요구사항 기능 명세서 작성
- 데이터베이스에 대한 사용자의 요구사항을 수집하고 분석
2. 개념적 설계
ERD 생성
DB 구성하는데 필요한 개체, 속성, 개체 관의 관계 추출
개체와 속성 추출 → 요구사항에서 개체는 대부분 명사로 이뤄져있지만, 속성과 구별하여 추출
개체 간의 관계를 정의
설계를 기반으로 ERD 생성 (ERD 표준기호 참고)
3. 논리적 설계
모든 개체 및 N:M관계는 릴레이션으로 변환
개체 → 테이블속성
1:N 관계 및 1:1 관계는 외래키(FK)로 표현
관계 : 릴레이션 이름, 관계속성 → 릴레이션 속성
다중 값 속성은 별도의 독립 릴레이션(Table)로 변환
4. 물리적 스키마 및 구현
반정규화 개념
어떤 경우에 반정규화를 사용하는가?

## DB 정규화?
데이터 모델의 중복을 최소화하고 데이터의 일관성, 유연성을 확보하기 위한 목적으로 데이터를 분해하는 과정
## 반정규화란?
정규화된 엔티티타입, 속성, 관계를 시스템의 성능향상과, 개발과 운영의 단순화를 위해 모델을 통합하는 프로세스 = 조금 어긴다
같은 데이터가 여러 테이블에 걸쳐 존재하므로 무결성이 깨질 우려가 있다. ⇒ 적당한 수준의 타협이 필요
1. 테이블 반정규화 방법
1:1 관계 / 1:N 관계의 테이블병합
수퍼/ 서브 타입 테이블 병합
수직 / 수평분할
테이블 추가
2. 대표적 반정규화 - 컬럼 반정규화
중복컬럼 추가 (자주 조회하는 컬럼이 있는 경우)
파생 컬럼추가 (미리 계산한 값)
PK에 의한 컬럼 추가
응용시스템 오작동을 위한 컬럼추가(이전데이터 임시보관)
3. 대표적 반정규화 - 관계 반정규화
중복관계추가 - 관계를 중복해서 조회경로를 단축
⇒ 정규화와 반정규화 둘 중에 뭐가 좋냐 : “케바케다”

⇒ 반정규화가 간단하게 무엇이냐? : 데이터 중복을 허용하고 조인을 줄이는 데이터베이스의 성능향상 방법입니다. 

⇒ 반정규화도 DB튜닝의 한 방법이다.

⇒ 프로젝트 진행시 3정규화까지 진행하면 좋다.

핵심 : 설계를 꼼꼼히 하자. 반정규화는 데이터베이스의 성능향상 방법이다.