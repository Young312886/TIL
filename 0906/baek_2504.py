colon = input()
stack = 1
result = 0
add = False
dick = {")":"(","]":"["}
que = []
j = 1
for i in colon:
    if i in dick:
        if que:
            k = que.pop()
            if k.isdigit():
                j = int(k)
                k = que.pop()
            if k != dick[i]:
                result = 0
                break
        else:
            result = 0
            break
        if add == False:
            result += stack
        stack /= 2 if k == "(" else 3
        stack /= j
        j = 1
        add = True
    elif i == "(":
        stack *= 2
        add = False
        que.append(i)
    elif i == "[":
        stack *= 3
        add = False
        que.append(i)
    elif i.isdigit():
        stack *= int(i)
        if not que:
            result = 0
            break
        que.append(i)
    # print(stack, result)
if que:
    result = 0
print(int(result))