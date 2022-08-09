# 1712 
# a,b,c = map(int,input().split())
# result = 0
# if c > b:
#     result = a//(c - b) + 1
# else :
#     result = -1
# print(result)

# 2292
# 1 7 19 37 은 + 6 + 12 + 18 즉, 6*n

# a = int(input())
# n = 0
# while a > 1:
#     n += 1
#     a = a - 6 * n
# print(n+1)

# 1193
# 1/1 // 1/2 2/1 // 3/1 2/2 1/3 // 1/4 2/3 3/2 4/1 //

# a = int(input())
# n = 0
# result = 0
# while a >= 1:
#     n += 1
#     a = a - n
#     if a < n+1:
#         if a == 0:
#             a = n
#             n -= 1
#         if n % 2 != 0:
#             result = f"{a}/{n+2-a}"
    
#         else :
#             result = f"{n+2-a}/{a}"
#         break   
# print(result)

# 2869 ## 시간제한으로 인한 수식화가 필수

# a,b,v = map(int,input().split())
# n=(v-b-1)/(a-b)+1
# print(int(n))