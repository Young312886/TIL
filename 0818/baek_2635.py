F = int(input())

'''
시작 / 두번째 
이후는 재귀로
x1, x2 / x3 = x1 - x2 ... 최대 길이 n을 추가 시켜 버리면 안됨
'''
def numbering(start,i,list1):
    if start - i < 0:
        return list1
    else:
        list1.append(start-i)
        return numbering(i,start-i,list1)
result = []
for k in range(0,F+1):
    list1 = [F,k]
    q = numbering(F,k,list1)
    if len(q) > len(result):
        result = q
print(len(result))
print(*result)