# M:N
## many-to-many relationships
- source & target
  - source : 관계 필드를 가진 모델
  - target : 관계 필드를 가지지 않은 모델
  - 즉, source 가 target을 참조함
## n:1 의 한계
- 기존의 모델에는 동일한 환자를 하나 더 만들어서 다른 참조를 만들어야 함
- 하나의 행이 여러 행을 참조하는 방법은 통하지 않음
- 결국, 하나의 테이블을 새로 만들어 새로 참조를 한다면?

## 중개 모델
- 각각의 테이블에서 외래키를 삭제
- 별도의 예약 모델을 새로 작성
- 이러면 각각의 테이블에서 역참조를 통해 다른 참조를 확인 가능

## ManytoManyField
- 한곳에 ManytoManyField 를 작성해주면, 
- 알아서 외부 중개 모델을 구성해줌
- 기존의 참조 테이블에는 외래키는 형성되지는 않음
- 중요한건 참조와 역참조의 관계(변수 이름이 변화하므로)
- 하지만, 두 변수 관계는 종속의 관계가 아니므로
- 각자 어느 방향으로든 새로 중개 테이블에 데이터 삽입 가능

### 삭제
- 이제 remove()를 사용하면 target에서도 관계를 삭제할 수 있음
- 당연히 source에서도 remove 가능
### 데이터 추가(외래키가 2개 이상) 및 직접 작성 시도
- through 옵션을 사용하여 지정할 수 있다
- manytomanyfield 안에 through 옵션 작성
- through_default를 통해 target에서도 생성 가능
### ManytoManyField
- to (target)
- options can be added
- we can change the table name by dding db_table arguments
- related_name
  - 참조시 변수 이름 설정
- through
  - 중개 테이블을 직접 설정시, 작성
- symmetrical
  - 재귀 참조시, on self 시에만 사용 가능
  - false로 설정시, 역의 관계가 형성되지 않음(기본세팅은 대칭관계가 형성됨)
  - 팔로우 데이터 테이블을 생각해주면 된다
## Django - user_like
- 위의 방식대로 그냥 입력 시, 역참조 변수 이름이 동일하여 충돌이 발생하는 오류 발생(다른 참조이지만)
- 따라서 related_name을 설정시켜야 한다
- 