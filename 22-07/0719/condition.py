# 백준 조건문 단계 해답
#1330
# a, b = map(int, input().split())
# if a > b:
#     print(">")
# elif a < b:
#     print("<")
# else : 
#     print("==")

#9498

# a = int(input())
# if a >= 90:
#     print("A")
# elif a >= 80 :
#     print("B")
# elif a >= 70:
#     print("C")
# elif a >= 60:
#     print("D")
# else :
#     print("F")


# # 2753

# a = int(input())
# #4 배
# if a % 4 == 0:
#     if a % 100 != 0:
#         result = 1
#     else :
#         if a % 400 == 0:
#             result = 1
#         else :
#             result = 0
# else :
#     result = 0
# print(result)

# # 14681

# x = int(input())
# y = int(input())
# result = 0
# if (x*y>0)& (x>0):
#     result = 1
# if (x*y>0)& (x<0):
#     result = 3
# if (x*y<0)& (x>0):
#     result = 4
# if (x*y<0)& (x<0):
#     result = 2
# print(result)

# #2884
# h,m = map(int,input().split())

# if m < 45:
#     if h == 0:
#         h = 24
#     h -= 1
#     m = m + 60 - 45
# else : 
#     m -= 45

# print(h,m)

# 2525
# h,m = map(int,input().split())
# t = int(input())

# m = m+t
# if m >= 60:
#     k = m // 60
#     j = m % 60
#     h = h + k
#     m = j
# if h >= 24:
#     h -= 24
# print(h,m)

# 2480

# a,b,c = map(int, input().split())
# result = 0
# if a == b == c:
#     result = 10000+a*1000
# else :
#     if a == b:
#         result = 1000 + a * 100
#     elif a == c:
#         result = 1000 + a * 100
#     elif b == c:
#         result = 1000 + b * 100
#     else : 
#         result = max(a,b,c)*100
# print(result)