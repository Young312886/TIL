from collections import defaultdict
d = [(0,1),(0,-1),(-1,0),(1,0)]
for tc in range(int(input())):
    n = int(input())
    atoms = defaultdict(list)
    for i in range(n):
        xi, yi, direct, energy = map(int, input().split())
        atoms[(xi*2,yi*2)] = [direct, energy]
    # 충돌 해야 한다
    # 좌표가 동일한가?
    # 시간 변화에 따른 좌표 충돌 계산?
    # 아니 , 좌표 변화 이후 충돌 계산
    # 다만, .5 방지를 위해 2배로 만들어 버림
    result = 0
    while atoms:
        new = defaultdict(list)
        erase = []
        for x,y in atoms.keys():
            direct, energy = atoms[(x,y)]
            xi, yi = d[direct]
            if -2001 <= x + xi <= 2001 and -2001 <= y + yi <= 2001:
                if new[(x+xi,y+yi)]:
                    direct1, energy1 = new.pop((x+xi,y+yi))
                    result += (energy1 + energy)
                    new[(x+xi,y+yi)] = [direct1, 0]
                    erase.append((x+xi,y+yi))
                else:
                    new[(x+xi, y+yi)] = [direct, energy]
        for key in set(erase):
            new.pop(key)
        atoms = new
    print(f'#{tc+1} {result}')

