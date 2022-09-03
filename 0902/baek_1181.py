result = []
for _ in range(int(input())):
    result.append(input())
result = list(set(result))
n = len(result)
for i in range(n-1):
    for j in range(i+1,n):
        if len(result[i]) > len(result[j]):
            result[i], result[j] = result[j], result[i]
        elif len(result[i]) == len(result[j]):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]
for k in result:
    print(k)

# python의 시간초과 피하기
n = int(input())
lst = []

for i in range(n):
    lst.append(input())

lst.sort()	## 괄호 안에 아무 값도 넣지 않으면 알파벳 순서대로 정렬을 해 준다.
lst.sort(key = len)	## 문자열 길이 순으로 정렬.

for i in lst:
    print(i)