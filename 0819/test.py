
nums = list(map(int, input().split()))
k = 0
for i in nums:
    print(i**2, i^2)

asc = [1,2,3,4,5,6,7,8]
dex = [8,7,6,5,4,3,2,1]
nums = list(map(int, input().split()))
if nums == asc:
    print('ascending')
elif nums == dex:
    print('descending')
else:
    print('mixed')
