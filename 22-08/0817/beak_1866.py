for _ in range(int(input())):
    case, target = map(int,input().split())
    cases = list(map(int,input().split()))
    index_num = [i for i in range(case)]
    deq = []
    while cases:
        comp = max(cases)
        new = cases.pop(0)
        place = index_num.pop(0)
        if new == comp:
            deq.append(place)
        else:
            cases.append(new)
            index_num.append(place)


    print(deq.index(target)+1)
