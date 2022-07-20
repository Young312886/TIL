# # 10818

# a = int(input())
# c = list(map(int, input().split()))
# max_num = -1000000
# min_num = 1000000
# for k in c:
#     if max_num < k:
#         max_num = k
#     if min_num > k:
#         min_num = k
        
# print(f"{min_num} {max_num}")

# # 2562
# max_num = 0
# for i in range(1,10):
#     k = int(input())
#     if max_num < k:
#         max_num = k
#         place_num = i
# print(max_num)
# print(place_num)

# # 2577
# a = int(input())
# b = int(input())
# c = int(input())

# k = str(a*b*c)
# l = [0]*10
# for j in k:
#     l[int(j)] = l[int(j)] + 1
# for p in l:
#     print(p)

# # 3052
# rest_num = set()
# for i in range(10):
#     a = int(input())
#     k = a % 42
#     rest_num.add(k)
# print(len(rest_num))

# # 1546

# a = int(input())
# score = list(map(int,input().split()))
# M = max(score)
# sum_num = 0
# for s in score:
#     sum_num += s/M*100
# print(sum_num/a)

# 8958

# t = int(input())
# for i in range(t):
#     case = input()
#     score = 0
#     n = 1
#     for j in case:
#         if j == "O":
#             score += n
#             n += 1
#         else :
#             n = 1
#     print(score)
    
# 4344

t = int(input())
for i in range(t):
    k, *score = map(int,input().split())
    aver_num = sum(score)/k
    n = 0
    for j in score:
        if j > aver_num:
            n+=1
    print(f"{(n/k)*100:.3f}%")