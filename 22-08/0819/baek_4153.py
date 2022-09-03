while True:
    trian = list(map(int, input().split()))
    if trian[0] == 0 & trian[1] == 0 & trian[2] == 0:
        break
    for i in range(3):
        for j in range(2,i,-1):
            if trian[i] > trian[j]:
                trian[i], trian[j] = trian[j], trian[i]

    if trian[2]**2 == trian[1]**2 + trian[0]**2:
        print('right')
    else:
        print('wrong')