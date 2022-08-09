def productExceptSelf(nums):

    result = []
    #앞으로 곱하기 * 뒤로 곱하기 = 앞뒤 곱
    #앞으로 곱하기 = 0,1,12,123,1234
    #뒤로 곱하기 = 0,5,54,543,5432
    # 각 결과 1: 2345(0*5432) 2: 1345(1*543) 3: 1245 (12*54) 4 : 1235(123*5) 5 : 1234 (0*1234)
    forward = []
    short = 1
    long = len(nums)
    for i in range(long):
        forward.append(short)
        short *= nums[i]
    backward = []
    short = 1
    for j in range(long-1,-1,-1):
        backward.append(short)
        short*=nums[j]
    for k in range(long):
        multi = forward[k] * backward[long-1-k]
        result.append(multi)
    return result
        
nums = [1,2,3,4]
productExceptSelf(nums)


### 1978 -baekjoon

# 소수 찾기
# def decimal(x):
#     if x == 1:
#         return False
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#     else:
#         return True

# t = int(input())
# nums = list(map(int,input().split()))
# result = []
# for i in nums:
#     result.append(decimal(i))
# print(sum(result))

## 2581

m = int(input())
n = int(input())
result = []
for i in range(m,n+1):
    if i == 1:
        continue
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        result.append(i)
if len(result) == 0:
    print(-1)
else: 
    print(sum(result))
    print(min(result))