n,t = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
lt, rt = 0, trees[-1]
# 최고 높이에서 하나씩 빼간다
result = 0
def binary(left, right):
    global result
    if left <= right:
        middle = (left+right) // 2
        output = sum(i-middle for i in trees if i > middle)
        # print(left, middle, right)
        if output >= t:
            binary(middle+1, right)
        else:
            binary(left, middle-1)
    else:
        result = right
binary(lt, rt)
print(result)