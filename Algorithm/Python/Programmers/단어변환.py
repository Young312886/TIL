def solution(begin, target, words):
    answer = 0
    n = len(words)
    word_len = len(begin)
    if target not in words:
        return 0
    words = [begin] + words + [target]
    graph = [[0] * (n+2) for i in range(n + 2)]

    for i in range(0, n + 2):
        origin = words[i]
        for j in range(1, n+2):
            change = words[j]
            diff = 0
            for k in range(word_len):
                if diff >= 2:
                    break
                if origin[k] != change[k]:
                    diff += 1
            if diff == 1:
                graph[i][j] = 1
    
    stack = [0]
    visited = [1] * (n+2)
    phase = 0
    while stack:
        # print(stack)
        # print(visited)
        node = stack.pop(0)
        phase += 1
        if node == n+1:
            return visited[node] - 1
        for new in range(n+2):
            if graph[node][new] == 1 and visited[new] == 1:
                visited[new] += visited[node]
                stack.append(new)
    
    return answer