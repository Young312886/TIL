## Stack
### 특징
- 후입선출
- 파이썬의 pop, append기능을 활용한다면 list에서 비슷하게 구현할 수 있다
- 특히 함수의 변수 활용과 정보 활용과 관련해서 파이썬에서 적극적으로 활용중에 있다
### overflow / underflow
- 지정된 사이즈를 초과하는 데이터를 입력 시 overflow가 발생
- 반대로 더이상의 데이터가 없지만 호출을 하게 된다면 underflow가 발생


## 재귀 함수
### 특징
- 자기 자신을 불러오는 함수 (call이기에 번역이 불러온다고 되어 있다)
- 더욱 효율적인 방식의 알고리즘인 동적 프로그래밍이 존재
  - 그 중에 memoization방식을 활용하여 구현 하는 방법도 있다
- 또한 일반적으로 재귀 함수는 목표값을 입력하는 방식으로 함수를 표현하는 것이 더 좋다

### Dynamic Programming
- 동적 계획 알고리즘
- 최적화 문제를 해결하는 알고리즘이다
- 입력 크기가 작은 부분 문제들을 우선적으로 해결뒤, 이에 기초하여 큰 크기의 문제들을 해결한다.
- 즉, 재귀 함수 중에서도 부분구조로 이뤄져 있다면 충분히 활용이 가능하다
- 아래서 위로 가는 바텀 업 / 위에서 아래로 가는 탑다운 방식 2개가 있다
- 알고리즘을 적용할 때 주로 테이블이 등장 (저장장소)
- DP의 구현에 재귀적 구조보다 반복적 구조로 구현하는 것이 더 효율적이다

### DFS (깊이 우선 탐색)
- 재귀 호출을 활용한 탐색
- 비선형 구조 그래프 탐색시 모든 조건을 탐색해야 함
- 출발점에서 갈수 있는 방향의 한쪽으로 모두 간 뒤에 더이상 진행이 불가능하면 가장 마지막에 만난 갈림길로 돌아가서 탐색 목표점에 도달할때까지 이를 반복하는 순회 방법
- 이러한 갈림길로 반환하는 과정은 stack을 활용 가능하다!!
- 또는 재귀 호출로 갈림길로 돌아갈 수 있다
- 방법 (stack사용)
  1. 시작 정점 v를 결정
  2. 정점 v에서 인접한(갈 수 있는) 정점 중에
     1. 방문하지 않은 정점w 를 스택에 push (그리고 이를 반복)
     2. 다 방문했으면 방향을 전환, stack에 pop하여 갈수 있는 곳이 존재할 때 까지 돌아감
  3. 스택이 공백이 될 때 까지 반복(모든 정점을 다 방문)
- 방문의 경우 t/f의 bool의 리스트로 만듬 (visited false면 거기로 간다)
- 경로의 경우 stack에 쌓으면 된다 (visited 가 true면 stack.pop)
- 인접의 경우의 저장하는 방법은 2차원으로 저장 (A : [ B,C ], A를 인덱스로 한 2차원 리스트를 저장해 두면 call할 수 있음)
- [예시코드](dfs.py)

~~참고로 오늘부터 hyperlink다는 법을 알아왔다~~

### 추가 백준 풀이
1. [백준 1966](https://www.acmicpc.net/problem/1966) [풀이](beak_1866.py)
   * 데크의 선입선출과 동시에 뒤에다 붙이는 과정을 추가로 구현하였다
   - 다만, 효율적이지 못한 변수 사용과, 기존의 인덱스의 위치로 출력 순서를 맞추려는 시도는 효율적이지 못한거 같다
2. [백준 2606](https://www.acmicpc.net/problem/2606) [풀이](baek_2606.py)
   - asdf