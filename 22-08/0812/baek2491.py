k = int(input())
num_list = list(map(int, input().split()))
result = 1
upper, down = 1, 1
for i in range(k-1):
    if num_list[i] <= num_list[i+1]:
        upper += 1
        result = max(result, upper)
    else:
        upper = 1
    if num_list[i] >= num_list[i+1]:
        down += 1
        result = max(result, down)
    else:
        down = 1
print(result)