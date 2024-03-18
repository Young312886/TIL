from itertools import combinations

def solution(lines):
    answer = []
    # 라인의 쌍에서 발생할 수 있는 모든 점의 종류
    line_pairs = list(combinations(lines, 2))
    dots = []
    for dot1, dot2 in line_pairs:
        a, b, e = dot1
        c, d ,f = dot2
        x = (b * f - e * d) 
        y = (e * c - a * f) 
        under = (a * d - b * c)
        if under != 0 and x % under == 0 and y % under == 0: # 두 선이 평행 & 정수값
            dots.append((y // under, x // under))
    # m * n box
    minx, miny = 1000, 1000
    maxx, maxy = -1000, -1000
        
    for dot in dots:
        dx, dy = dot
        minx = min(dx, minx)
        maxx = max(dx, maxx)
        miny = min(dy, miny)
        maxy = max(dy, maxy)
        
    x = maxx - minx
    y = maxy - miny
    lines = [["." for _ in range(y+1)] for _ in range(x+1)]
    # if m == 0:
    #     lines = [["." for _ in range(n+1)] for _ in range(m+1)]
    # print(dots, rx,lx, ry, ly, addx, addy)
    # print(lines)
    # 0 > 4, -4 > 0, 4 > 8 x + 4
    # 4 > 0, -4 > 8,
    # 0, 4 = 0, 4 / -4, -4 = 8, 0 / 4, -4 = 8, 8
    for dot in dots:
        dx, dy = dot
        print(dx - minx,  dy - miny)
        lines[dx - minx][ dy - miny] = "*"
    for line in lines:
        answer.append(''.join(line))
    return answer