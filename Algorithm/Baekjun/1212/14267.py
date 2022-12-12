n, m = map(int, input().split())

workers = [0] * (n+1)
headers = [0] + list(map(int, input().split()))
# 트리 순회를 위해 자식의 번호를 나타내는 방법으로 전환
# tree = [[] for _ in range(n+1)]
# for i in range(n+1):
#     if headers[i] == -1:
#         continue
#     tree[headers[i]].append(i)
for _ in range(m):
    worker, power = map(int, input().split())
    workers[worker] += power
# 직속 상사의 번호는 자신의 번호보다 작으며, 최종적으로 1번이 사장이다
for i in range(1,n+1):
    if headers[i] == -1:
        continue
    workers[i] += workers[headers[i]]
print(*workers[1:])