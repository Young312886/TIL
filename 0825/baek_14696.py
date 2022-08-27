for _ in range(int(input())):
    a, *a_pic = map(int, input().split())
    b, *b_pic = map(int, input().split())
    a_li = [0]*5
    b_li = [0]*5
    for star in a_pic:
        a_li[star] += 1
    for star in b_pic:
        b_li[star] += 1
    result = "D"
    for i in range(4,0,-1):
        if a_li[i] > b_li[i]:
            result = "A"
            break
        elif a_li[i] < b_li[i]:
            result = "B"
            break
    print(result)