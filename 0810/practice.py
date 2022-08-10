# di = [0,1,0,-1]
# dj = [1,0,-1,0]
# n = 3
# m = 4
# arr = [[1,2,3,4],[5,6,7,8]]
# for i in range(n):
#     for j in range(m):
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0<=ni<n and 0<=nj<m:
#                 print(ni,nj)


## 부분집합 생성 및 확인
#
# arr = [3, 6, 7]
# n = len(arr)
#
# for i in range(1 << n):
#     for j in range(n):
#         if i & (i << j):
#             print(arr[j], end=' ')
#     print()
#     print()

arr = [1,2,3]
result = []
for i in range(1<<len(arr)):
  subset = []
  for j in range(len(arr)):
    if i & (1<<j):
      subset.append(arr[j])
  result.append(subset)
print(result)