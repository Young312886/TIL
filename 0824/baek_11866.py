k, n = map(int, input().split())
target = list(range(1,k+1))
visit = [0]*k
stack = []
while len(stack) < k:

