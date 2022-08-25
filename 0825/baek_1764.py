import sys
n, m = map(int, input().split())
hear = list(sys.stdin.readline().strip() for _ in range(n))
look = list(sys.stdin.readline().strip() for _ in range(m))
result = list(set(hear) & set(look))
result.sort()
print(len(result))
for j in result:
    print(j)