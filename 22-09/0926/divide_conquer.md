## 분할 정복
- 문제를 작은 부분으로 나눠 각각을 해결한다
- 이후 해결된 해답을 모은다 = 통합
### 병합 정렬
- 2개의 부분집합을 정렬하면서 하나의 집합으로 병합
- 포인터와 유사한 방식으로 작은 것을 넣어주고 이후 옆으로 하나 진행(크기 비교 대상은 현재 포인터끼리만)
### 퀵 정렬
- 피봇값이 기준이 된다
- 이후, 포인터를 두개부여, 그 포인터 간의 크기 비교를 진행
- 변화를 준다
- Hoare-Partition 알고리즘 이다
- 외에도 다양한 방법이 존재(파티션의 조건에 따라)
- Lomuto Partition 알고리즘
- p에서 r 사이, r이 파티션으로 주어지고,  그사이의 값들을 정렬(오른쪽이 정렬됨)
### 이진 검색
- 자료의 가운데있는 항목을 주어지고, 다음 검색 위치를 결정
- 검색 범위를 반으로 줄여가면서 진행
- 단, 자료가 정렬된 상태여야 만 한다