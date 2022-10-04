# DataBase
데이터를 다루는 기술
1. 파일을 이용한 데이터 관리
  - 운영체계  상관 없이 관리 가능
  - 송수신이 가볍다
  - 다만, 대용량 데이터에는 부적합
  - 구조적 정리에는 어렵다
  - 확장 또한 불가능
2. 스프레드시트를 활용
   - 컬럼, 레코드를 통해 구체적 데이터 정리
3. 데이터베이스의 등장
   - 프로그래밍 언어를 통해 작동시킨다
   - RDB 라는 관계형 DB를 많이 사용
   - 스프레드시트의 모음으로 이해해도 좋다
## DataBase
- 체계화된 데이터의 모임
- 통합 관리 되는 정보의 집합
- 검색, 구조화 와 같은 작업에 도움됨
- Database Management System(DBMS)
- 데이터 베이스 관리 시스템 : Oracle, MySql, Sqlite 등등
- 관계형 db의 장점 : 직관적, 쉬운 접근, 대용량을 효율적 관리
## SQL
- Structured Query Language
- 특수 목적의 프로그램 (RDBMS를 위한)
- 스키마 생성, 자료 검색 및 관리 까지
### SQL 명령어
1. DDL(Definition) - 구조 정의
2. DML(Manipulate) - 데이터 조작(CRUD)
3. DCL(Control) - 보안, 권한, 수행 제어 등 (SQLite 에서는 미지원)

### Syntax
- 키워드로 시작, ; 로 문장 끝남
- 대소문 구분이 없긴 한데, 대문자로 최대한 적어주자

## DDL
### Constraints
```sql
CREATE TABLE contacts(
   name TEXT NOT NULL,
   age INTEGER NOT NULL,
   email TEXT NOT NULL
);
```
#### 다양한 Data Types
  - null
  - integer 
  - real
  - text
  - blob(Binary Large Object), 이미지 파일 등
- 다만, sqlite의 경우 입력되는 데이터에 맞춰서 type 이 변화된다(유연하게)
- 타입 선호도
  - Sqlite 에선 다양한 타입을 지원하지는 않음
  - 다만, 위의 타입들로 치환하여 받아들임
  - 다른 db간의 호환성을 최대화 하기위한 방식
#### 데이터 무결성
- 데이터의 정확성, 일관성을 위한 제약 조건들
1. not null
   - 칼럼에 null 값이 혀용되지 않도록
2. unique
   - 서로 중복되지 않도록, 고유값이 되도록 함
3. primary key
   - 고유값을 주는 컬럼
   - 암시적으로 not null 포함됨
   - 다만, integer 에만 사용 가능
4. autoincrement
   - primary 랑 같이 사용 가능
   - 삭제된, 사용되지 않는 값 재사용 불가능 하게 만드는 것
   - Django 의 id칼럼에 자동 적용
5. 기타  

#### Alter Table
1. rename table
2. rename column
3. add new column
4. delete column
- 만약, add 하는 과정에서 기존 데이터에서의 not null 불충족과 충돌이 발생하면,
- default 값을 끝에 지정해줘서 오류 방지를 할 수 있음
- 삭제 불가능한 조건
  - 다른 테이블이 참조하고 있는 경우
  - primary key column의 경우
  - unique 제약 조건이 걸려 있는 경우

### DML
```sql
.open mydb.sqlite3
create table users(
   <!-- ~~~ -->
)
.mode csv
.import user.csv users
-- 만든 테이블에 csv 파일을 입력해준다

```
#### Read Data
- select - from table
  - 테이블에서 특정 데이터 조회
- order by (asc, desc)
  - 조회 이후 데이터 정렬 순서 지정 가능
- select distinct
  - select 바로 뒤에, 중복 지정할 column 지정
  - 중복 행들이 삭제됨, order 도 가능
- where
  - condition을 만족하는 해당 column들을 선택 가능
  - delete update에도 사용 가능
  - 연산자(like, between, =, in) 사용 가능
- limit
  - 결과 갯수 제한
- offset
  - 특정 위치에서 부터의 데이터를 조회하는 방법으로 변환
- group by
  - 특정 값을 기준으로 그룹화 가능
  - count(*) 를 통해 갯수 출력 가능
  - avg(column) 또한 평균 출력 가능 

#### Changing Data
- insert / update / delete
- insert
  - insert into table (...) values (///)
  - 새 행 삽입
  - 쉼표로 모든 value 작성
  - column 은 생략 가능하지만, 모든 칼럼에 대한 value를 입력해줘야 한다
  - 여러 행을 넣기 위해선, ()로 구분하여 여러줄 삽입 가능
- update
  - update ___ set col = value  where rowid = __ (다른걸로도 가능)
  - where 없으면 전체 변환
- delete
  - delete from table where __;
  - where 없으면 모든 행 삭제
  - order by, limit,like 로 여러줄 삭제 가능
  - 