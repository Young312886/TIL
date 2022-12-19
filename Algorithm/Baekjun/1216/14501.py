import sys
input= sys.stdin.readline
n = int(input())

profit = [0] * (n+1)
stack = 0
for i in range(1,n+1):
    t, p = map(int, input().split())
    stack = max(stack, profit[i-1])
    if i+t-1 <= n:
        if profit[i+t-1] < (stack+ p):
            profit[i+t-1] = stack + p
print(max(profit))