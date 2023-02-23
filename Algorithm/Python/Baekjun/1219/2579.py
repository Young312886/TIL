import sys
input = sys.stdin.readline
n = int(input())
stairs = [int(input()) for _ in range(n)]
def db():
    if len(stairs) <= 2:
        return sum(stairs)
    else:
        stack = [[0,0]] * n
        stack[0] = [stairs[0], 0]
        stack[1] = [stairs[0]+ stairs[1], stairs[1]] 
        for i in range(2,n):
            stack[i] = [stack[i-1][1]+stairs[i], max(stack[i-2]) + stairs[i]]
    return max(stack[-1])
print(db())


