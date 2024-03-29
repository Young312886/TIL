## 스택을 활용한 계산기 구현
- eval()함수의 구현
### 주어진 문자열의 연산을 시행
- 중위 표기법을 우리는 후위표기법으로 변환할 것이다
- 우선순위가 높으면 스택에 push하고 낮은것이 앞에 있으면 pop해서 문자열에 추가하는 방식
- 우선순위를 잘 부여하자
  
### 후위 표기법의 수식을 스택으로 다시 계산
- 위의 방식과 반대로 모든 피연산자를 스택에 저장
- 연산자가 나오면 피연산자를 pop해가며 오른쪽에 왼쪽으로 계산

## BackTracking
- 해를 찾는 도중 막히면 되돌아가서 다시 찾는다
- 최적화 문제(가장 짧은)와 결정 문제(존재 여부)를 해결할 수 있다
- 결정 문제 => 해가 존재하는지의 여부
  - 미로
    + 스택에 진행사항을 저장해 나간다
    + 이후에 만약 진행 방향이 더이상 없을 시 pop을 통해 뒤로 돌아간다
  - n-Queen
  - Map coloring
  - 부분집합의 합
- 이렇듯 노드의 유용성을 탐색 후, 진행 또는 되돌아감 결정
- 가지치기를 통애 유용하지않은 노드들을 버리기 때문에 모든 후보 탐색이 아니다
- #### Backtracking 탐색 구조
- 우선 상태 공간트리의 깊이 우선 탐색 실시
- 노드의 유망성 점검
- 검색 실시

### BackTracking을 활용한 부분집합 생성

- [단순 표현]('stack_subset.py')
- [부분집합의 합]('stack_subset2.py')