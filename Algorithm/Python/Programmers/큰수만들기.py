def solution(number, k):
    stack = list(int(i) for i in number)
    situation = [0] * len(number)
    while k:
        before = 10
        delete = 0
        # print(stack)
        for i, num in enumerate(stack):
            if situation[i] == 0:
                if num > before:
                    k -= 1
                    situation[i-1] = 1
                    delete = 1
                    break
                else:
                    before = num
        # if delete == 0:
        #     stack.index(min(stack))
        #     k -= 1
        answer = [num for i,num in enumerate(stack) if situation[i] == 0 ]
    return ''.join(map(str,answer))