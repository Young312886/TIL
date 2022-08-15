for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())
    # 우선 접점이 없는 친구들
    if x1 > p2 or p1 < x2 or y1 > q2 or q1 < y2:
        print('d')

    # 접점이 한 점이 친구들
    elif                    :
        print('c')

    # 접점이 한 선인 친구들
    elif                :
        print('b')
    # 아닌 놈들 = 면이다
    else:
        print('a')