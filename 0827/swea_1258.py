import sys
sys.stdin = open('input (1).txt')

'''
풀이법
우선, 한줄에 숫자가 적혀있는 인덱스들의 범위를 stack을 통해 지정해 준다
그 다음, 그 줄에 있는 범위가 아래의 줄들과 비교해가면서 상자의 크기를 작성할 수 있다

이후 크기 비교를 통해 나름 괜찮게 정리해준다 (이게 문제가 아녔다)
'''

int(input())
for tc in range(1):
    n = int(input())
    ground = [[0] + list(map(int, input().split())) for _ in range(n)]
    d = [(0,1),(1,0)]
    i, j = 0,0
    result = []
    line_info = [[0] for _ in range(n)]
    # print(line_info)
    # print(ground)


    # 우선, 창고를 한줄씩 빼가면서 상자들이 있는 구간을 기록하겠다. line_info에 저장될 것이다
    while 0<= i < n and 0<= j <=n:
        if ground[i][j] != 0:                   # 만약 상자가 있을 경우
            if len(line_info[i]) %2 == 1:       # 현재 라인 정보의 모양이 짝이 안맞는 경우, 즉 처음 시작이거나 앞에 상자가 완료가 되었다면
                key = line_info[i].pop()        # 앞의 0을 빼주고
                line_info[i].append(j)          # 값을 2번넣어준다 (이는 가로 한자리 상자의 경우의 오류와 인덱싱을 편하게 하기 위함이다)
                line_info[i].append(j)
            else:
                line_info[i].pop()              # 만약 쌍이 맞는 상황이라면 앞의 숫자를 빼서 신규로 갱신한다 / 또는 한칸 증가이다
                line_info[i].append(j)

        elif ground[i][j] == 0:                 # 만약 0이라면
            key = line_info[i].pop()            # 0을 뒤에 붙여주는 작업이다
            if key == 0:
                line_info[i].append(key)
            else:
                line_info[i].append(key)
                line_info[i].append(0)
        j += 1
        i += j//(n+1)
        j = j % (n+1)
        if j == 0:
            line_info[i-1].append(0)            # 끝에 0을 더 붙여줘서 아래의 인덱스 오류를 방지
    # print(line_info)


    i, j = 0, 0
    while 0<= i < n:                            # line_info에서 이제 상자 크기들을 비교하는 과정을 거칠 것이다
        x = line_info[i][j]
        if x == 0:                              # 0이 뽑히면 다음줄로 넘어가야 함
            j = 0
            i += 1
        else:
            y = line_info[i][j+1]               # 이제 다음 인덱스도 불러옴
            k = 1
            while k<n-i:                        # 다음줄에 같은 모양의 숫자들이 있는지 확인
                if x in line_info[i+k] and y in line_info[i+k]:
                    line_info[i+k].remove(x)    # 여기서 remove를 하는 이유는 이후에 한줄씩 비교를 해가는 과정에서 이미 확인한
                    line_info[i+k].remove(y)    # 친구들을 skip하는 방법이 생각나지 않아서 그냥 삭제시켜버림
                    k += 1
                else:
                    break
            result.append([k,y-x+1])            # 다 찾았으면 그 가로와 세로를 result에 저장
            j += 2
    # print(result)
    for i in range(len(result)):                # 기준에 맞게 선택정렬
        for j in range(i+1,len(result)):
            x1, y1 = result[i]
            x2, y2 = result[j]
            if x1*y1 > x2*y2:                   # 우선 넓이 비교
                result[i], result[j] = result[j], result[i]
            elif x1*y1 == x2*y2:                # 같으면 가로 비교
                if x2 < x1:
                    result[i], result[j] = result[j], result[i]
    # print(result)                             # 든 생각, print를 저거 말고 다르게 했으면 되었을까?
    print(f'#{tc+1} {len(result)}', end=' ')
    for k in result:
        print(*k, end = ' ')
    print()



'''
0,4 
0,4
0,4
5,9
1,3 5,9
1,3 5,9
5,9
0
0
0

0,1
0
0,3
0,3
'''