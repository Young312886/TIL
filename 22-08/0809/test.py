## bus
T = int(input())
for tc in range(1, T + 1):
    K,N,M = map(int, input().split())        # N 총 길이 
    arr = list(map(int, input().split()))
    charger = [0]*N                          # 0 으로 구성된 리스트 먼저 뽑아준다 (버스 위치 뽑을라고)
    for i in arr:                            # [0,0,0,0,0,0,0,0,0,0]
        charger[i] = 1                       # [0,0,1,0... 이런 모양]

    start = 0                                #시작값
    maxp = 0 + K                             #갈 수 있는 거리
    cnt = 0                                  #결과값 

    while maxp < N:                          # 총 거리에 도달할 때 까지
        if start == maxp: '''스타트랑 갈수있는 지점이 같아지는건, start부터 진행 가능거리 사이에
                             charger가 없으므로 답이 아니라는 뜻'''
            cnt = 0              
            break                            #  탈출

        if charger[maxp] == 1:               #갈수 있는 거리에 1이 있으면 
            start = maxp                     #주행한 거리로 스타트를 초기화 
            maxp = start + K                 # 갈수 있는 거리 = 초기화된 스타트 + 거리
            cnt += 1                         # 충전햇으니 +1 

        elif charger[maxp] == 0:             # 혹시 차저가 없다면 
            maxp -= 1                        #현재갈수있는 거리에서 빼줘

    print(f"#{tc} {cnt}")