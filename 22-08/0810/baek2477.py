## 인덱스를 이리저리 바꾸는 것은 매우 안좋은 영향을 끼칠 수 있다
# 따라서 탐색할 수 있는 범위내의 것들을 가지고 와서 거기에 없다면 을 해도 되는 상황에선
# 그렇게 소거법으로 탐색을 진행해보자
fruit = int(input())
box = []
for _ in range(6):
    m, n = map(int, input().split())
    box.append([m,n])
w, w_idx = 0, 0
h, h_idx = 0, 0
for idx, head in enumerate(box):
    if head[0] == 1 or head[0] == 2:
        if w < head[1]:
            w = head[1]
            w_idx = idx
    else :
        if h < head[1]:
            h = head[1]
            h_idx = idx
index_list = [box[h_idx-1],box[(h_idx+1)%6],box[w_idx-1],box[(w_idx+1)%6]]
small = 1
for i in box:
    if not i in index_list:
        small = small * i[1]
result = (h*w - small)*fruit

print(result)