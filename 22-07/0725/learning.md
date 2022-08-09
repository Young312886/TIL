### Method 활용
* list. append ()
* 앞의 문자는 주어 / 뒤는 동사라고 이해하면 쉽다

#### string methods
- .find() 첫번째 위치(없으면 -1)
- .index() 첫번째 위치(단, 없으면 오류)
- .isalpha() 알파벳 여부 (유니코드 상 letter인가)
- .isupper() .islower() 대소문자
- .istitle() 타이틀(대문자 시작 + 소문자)
- .isdecimal / isdigit / isnumerical  숫자 / 수 / 수 표기법 (오른쪽으로 범위가 넓어짐)
- .replace( ,  []) 바꿀 대상을 바꿈, 횟수도 지정 가능
- .strip("") 문자 제거
- .split("") 문자 기준 분리
- 'separator'.join([]) iterable(리스트) 를 합침, 구분자로
- .capitalize() 첫문자 대문자
- .title() 문자열 띄어쓰기 기준 제목화(첫문자 대문자)
- .upper() .lower(). swapcase() 대 /소 /변경

#### List methods
- .append() 오른쪽에 삽입
- .insert(i,x) i에 x 삽입 
- .remove(x) 왼쪽의 x를 제거 (없는 거 삭제하면 오류)
- .pop(i) 없으면 마지막, 있으면 인덱스의 항목 반환 및 제거
- .extend() m 을 옆에 추가
- .index(x, start, end) index 숫자 반환(범위 내 제일 첫번째)
- .reverse() .sort() 역순 / 정렬
- .cont() 갯수 세기
#### Tuple
- we can use 'a in []'
- but As tuple is immutable, we can't much change over it

#### Set methods (중복이 불가능한 리스트)
- .copy() 얕은 복사
- .add()없으면 추가
- .pop() 반환 및 제거
- .remove() 삭제 / 없으면 에러
- .discard() s가 있으면 삭제 / 없으면 에러 안남
- .update(t) 없으면 추가
- .clear() 항목 제거
- .isdisjoint(t) 서로소인경우, True (교집합이 없을 때)
- .issubset(t) 하위면 True
- .issuperset(t) 상위면 True

#### Dictionary methods
- .clear() 제거
- .copy 복사
- .keys() .values() .items() 키 / 벨류 / 둘다
- .get(k)  k의 value 없으면  none (뒤에 추가하면 그 값을 리턴)
- .pop() 반환 및 삭제
- .update([]) 업데이트

### 얕은 복사와 깊은 복사 (Shallow & Deep)
- 복사는 할당 / 얕은 / 깊은 복사 3가지가 존재
  - 할당 (=)
    - 복사본이 발생 (같은 주소)
    - 이때의 복사본은 지속적으로 원본객체를 참조 (즉, 원본이 변화하면 복사본도 변화)
  - 얕은 복사 ([ : ])
    - 슬라이싱을 활용하여 연관 결과 복사 (다른 주소)
    - 다만, 만약 2차원 리스트의 형식으로 복사하게되면 이때는 주소를 참조하게 됨
  - 깊은 복사 (deepcopy)
    - copy에서 deepcopy를 활용하여 완전 복사 (다른 주소)
    - 다만 자주 사용하게 되면 메모리 사용량이 많이 증가