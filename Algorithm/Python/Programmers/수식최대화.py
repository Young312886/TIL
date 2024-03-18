# 연산자 집합 만들기
from itertools import permutations
oper = ["+","-","*"]
oper_subset = [list(i) for i in permutations(oper, 3)]
def solution(expression):
    answer = []
    # 연산자 집합 만들어서 순서대로 연산
    # 연산 리스트 구성
    base = []
    
    single_num = ""
    for i in expression:
        if i in oper:
            base.append(int(single_num))
            base.append(i)
            single_num = ""
        else:
            single_num += i
    base.append(int(single_num)) # 마지막 숫자 넣기
    # 연산자 순열모두 연산 시행
    for opers in oper_subset:
        calcul = base
        skip = False
        test = 0
        # 해당 차례의 연산자 연산 시행
        for op in opers:
            skip = False
            new_calcul = []
            for idx, single in enumerate(calcul):
                # print(single, op, new_calcul)
                if single == op and new_calcul:
                    a = new_calcul.pop()
                    b = calcul[idx + 1]
                    # print(type(a), type(b))
                    # new_calcul.append(a)
                    if single == "*":
                        new_calcul.append(a * b)
                    elif single == "-":
                        new_calcul.append(a-b)
                    elif single == "+":
                        new_calcul.append(a+b)
                    else:
                        new_calcul.append(a)
                    skip = True
                    test = 1
                else:
                    if skip == True:
                        skip = False
                    else:
                        new_calcul.append(single)
            calcul = new_calcul
            
        answer.append(abs(new_calcul[0]))
    
    
    return max(answer)