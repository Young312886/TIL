# def first(x):
#     n = 0
#     while x != 1:
#         if x % 3 == 0:
#             x = x / 3
#             n += 1
#         elif x % 2 == 0:
#             x = x / 2
#             n += 1
#         else:
#             x -= 1
#             n += 1
#     return n
# def second(a):
#     n1 = 0
#     while a != 1:
#         if a % 3 == 0:
#             a = a / 3
#             n1 += 1
#         else:
#             a -= 1
#             n1 += 1
#         if a % 2 == 0:
#             a = a/2
#             n1 += 1
#     return n1
# a = int(input())
# k = min(first(a), second(a))
# print(k)
# 위의 코드는 그냥 단순히 계산법들을 나열한 것이다

# 동적 프로그래밍을 활용한 작성법
# 상향식, 인데 안먹힌다
# def down(x, memo):
#     for i in range(3):
#         memo[i] = 1
#     if x <= 3:
#         return 1
#     if memo[x] == 0:
#         if x % 3 == 0 and x % 2 == 0:
#             memo[x] = min(memo[x//3], memo[x//2]) + 1
#         elif x % 3 == 0:
#             memo[x] = memo[x//3] + 1
#         elif x % 2 == 0:
#             memo[x] = memo[x//2] + 1
#         else:
#             memo[x] = memo[x-1] + 1
#     print(memo)
#     return memo[x]
# n = int(input())
# print(down(n,[0 for i in range(n+1)]))

# 틀렸다고 떴지만 아마 시간 초과 => 맞았다
# val의 초기 설정과 for문의 설정에서 오류가 있었다. 우선, val은 0부터 시작해야 한다. 인덱스로 값을 호출하는 것이므로 +1 이 되는 모양을 보여줘야 한다.
# 1은 이미 완성이므로 0을, 2,3은 계산해서도 1이 뜰꺼고 동시에 1이 나오려면 1에 주어진 값이 0이어야 잘 뜬다. 근데 그거 가지고 오류가 뜨려나...?
def down1(x):
    val = [0,0]
    if n >= 2:
        for i in range(2,n+1):
            if i % 3 == 0 and i % 2 == 0:
                val.append(min(val[i//3], val[i//2], val[i-1]) + 1)
            elif i % 3 == 0:
                val.append(min(val[i//3],val[i-1])+1)
            elif i % 2 == 0:
                val.append(min(val[i//2],val[i-1])+1)
            else:
                val.append(val[i-1]+1)
    # print(val)
    return val[n]

n = int(input())
print(down1(n))

# 아래는 힌트를 참고한 코드 / 효율이나 다른 측면에서는 위의 코드와 차이를 보이지 않는다
def down1(x):
    val = [0,0]
    if n >= 2:
        for i in range(2,n+1):
            val.append(val[i-1] + 1)
            if i % 3 == 0:
                val[i] = min(val[i], val[i//3] + 1)
            if i % 2 == 0:
                val[i] = min(val[i], val[i//2] + 1)
    # print(val)
    return val[n]

n = int(input())
print(down1(n))