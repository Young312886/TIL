from collections import deque
k = int(input())
stack = deque(range(1,k+1))
# print(stack)
while len(stack)>1:
    drop = stack.popleft()
    back = stack.popleft()
    stack.append(back)
print(stack[0])