# 10250

# h 만큼 반복해서 실시
# 총 객실은 h*w


# t = int(input())
# for i in range(t):
#     h,w,n = map(int, input().split())
#     if h == 1:
#         result = 100 + n
#         print(result)
#         continue
#     k = n // h + 1
#     j = n % h
#     if j == 0:
#         j = h
#         k -= 1
#     result = j * 100 + k
#     print(result)

# 2775

# k 층 n 호
 
# 0 -- 1 2 3 4 5 6 7 8 9
# 1 -- 1 3 6 10 ...
# 2 -- 1 4 10 25
# 3 -- 1 5 15

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    num_1 = list(range(1,n+1))
    for j in range(n):
        for p in range(1,k):
            num_1[p] += num_1[p-1]
    print(num_1[-1])

# 2839

