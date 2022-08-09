# # 11653
# def factorization(x):
#     d = 2
#     result = []
#     while d <= x:
#             if x % d == 0:
#                 result.append(d)
#                 x = x/d
#             else : 
#                 d += 1
#     return result
# t = int(input())
# result = factorization(t)
# for i in result:
#     print(i)


# # 1929
# m, n = map(int, input().split())
# result = []
# for i in range(m,n+1):
#     for j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#             break
#     else :
#         result.append(i)
# for k in result:
#     print(k)

# 4948
# result = []
# for i in range(1,123456*2+1):
#     for j in range(2,int(i**(1/2))+1):
#         if i % j == 0:
#             break
#     else : 
#         result.append(i)
# while True:
#     n = int(input())
#     prime = 0
#     if n == 0:
#         break
#     for k in result:
#         if n + 1 <= k and 2*n >= k:
#             prime += 1
#     print(prime)

# 9020
# prime_number = []
# for i in range(1,10000):
#     for j in range(2,int(i**(1/2))+1):
#         if i % j == 0:
#             break
#     else : 
#         prime_number.append(i)
# prime_number.sort()

# t = int(input())
# for test_caes in range(t):
#     n = int(input())
#     k = n / 2
#     i = 0
#     while True :
#         if k-i in prime_number and n-k-i in prime_number:
#             break
#         else :
#             i += 1
#     print(k-i, n-k-i)
            

# 10872
# def factorial(x):
#     if x == 1:
#         return 1
#     else :
#         return x * factorial(x-1)
# print(factorial(int(input())))

# 10870

# def fibonacci(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     else : 
#         return fibonacci(x-1) + fibonacci(x-2)

# print(fibonacci(int(input())))

# 17478

# def chatbot(x):
#     if x == 1:
#         print('''어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
# "재귀함수가 뭔가요?"
# "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# 그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."''')


# 2447


# def astronoid(m,k):
#     if not m:
#         star = k*3 + "\n" + k * 1 + " " * (n-m+1) + k * 1 + k * 3
#         print(star)
#         return
#     star = k*3 + "\n" + k * 1 + " " * (n-m+1) + k * 1 + '\n' + k * 3
#     print(star)
#     astronoid(m-1,star)
#     print("다음")

# n = int(input())
# astronoid(n,"*")

k = "*" * 3 + '\n' + '*' + " " + "*" + '\n' + "*"*3
print(k)
j = k * 3
print(j)