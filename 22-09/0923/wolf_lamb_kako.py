from collections import deque
def solution(info, edges):
    answer = 0
    tree = [[] for _ in range(len(info))]
    for i in edges:
        tree[i[0]].append(i[1])
    result = 0
    stack = deque()
    visited = [0] * len(info)
    def gathering(lamb, wolf, index):
        print(stack, index)
        nonlocal result
        if info[index] == 0:
            lamb += 1
        else:
            wolf += 1
        if lamb <= wolf:
            if stack:
                new = stack.pop()
                wolf -= 1
                for i in tree[new]:
                    if visited[i] == 0:
                        gathering(lamb, wolf, i)
                        visited[index] = 0
                else:
                     = stack.pop()
        visited[index] = True
        print(wolf, lamb)

    gathering(0,0,0)
    return result
print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))