def first(x):
    n = 0
    while x != 1:
        if x % 3 == 0:
            x = x / 3
            n += 1
        elif x % 2 == 0:
            x = x / 2
            n += 1
        else:
            x -= 1
            n += 1
    return n
def second(a):
    n1 = 0
    while a != 1:
        if a % 3 == 0:
            a = a / 3
            n1 += 1
        else:
            a -= 1
            n1 += 1
        if a % 2 == 0:
            a = a/2
            n1 += 1
    return n1
a = int(input())
k = min(first(a), second(a))
print(k)