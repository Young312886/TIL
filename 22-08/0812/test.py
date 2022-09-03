a = ['a','b','c','\0']
# string 의 길이 체크(c에서는 string의 마지막에 '\0'(null 문자)를 넣어줘야지) 작동하게 된다
def srtlen(a):
    n = 0
    while a[n] != '\0':
        n += 1
    return n

print(srtlen(a))

# 문자열 뒤집기
s = 'reverse the string'
s = list(s)
s.reverse()
print(''.join(s))

def reversing(s):
    k = len(s)
    p = [' ']*k
    for i in range(k//2+1): # 한개를 더 해야지 가운데 발생한는 문자 까지 커버 가능
        p[i], p[k-i-1] = s[k-i-1], s[i]
    return ''.join(p)
s = 'reverse'
print(reversing(s))

s = 'reversingadf'
rever = ''
for i in range(1,len(s)+1):
    rever = rever + s[-i]
print(rever)

# 문자열 비교 함수

def compare_string(x,y):
    if x == y:
        return 1
    elif x > y:
        return y
    else :
        return x
a = 'bbb'
b = 'aaa'
print(compare_string(a,b))

def my_strcmp(x,y):
    if len(x) == len(y):
        return 0
    elif len(x) > len(y):
        return -1
    else :
        return 1
str1 = 'abcasdfas'
str2 = 'abcasdasf'

print(my_strcmp(str1,str2))


# itoa

a = '1'
print(ord(a)) # 49

# print(chr(49), type(chr(49)))

a = 4872

## 음수일 경우
def itoa_minus(x):
    result = ''
    if x < 0:
        result = result + chr(45)
        x = x * (-1)
    while x != 0:
        i = x % 10 + 48
        x = x // 10
        result = chr(i) + result
    return result

print(itoa_minus(a), type(itoa_minus(a)))

def brute_force(pattern, target):
    N = len(pattern)
    M = len(target)
    j,i = 0,0
    while j < M and i < N:
        if target[j] != pattern[i]:
            i = i-j # 탐색 중 리셋 위치는 그 다음 위치
            j = -1 # 타겟의 경우 리셋 (이후 +1 할거라 -1 줌)
        i += 1
        j += 1
    if j == M:
        return i - M # 탐색된 인덱스 출력
    else :
        return -1

pattern = 'abebaba abc def'
target = 'abc'
print(brute_force(pattern,target))

def kmp_Search(pattern,target):
    N = len(pattern)
    M = len(target)
    arr = [0] * N
    i, j = 0, 0
    while i < N and j < M:
        if pattern[i] == target[j]:
            i += 1
            j += 1
            arr[i] = j
        else:
            if j == 0:
                i += 1
            else:
                i = arr[i-1]+1
                j = arr[j-1]
        if j == M:
            return i - M
    return -1
print(kmp_Search(pattern,target))