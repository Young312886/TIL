def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            stack = [i]
            visited[i] = 1
            while stack:
                node = stack.pop()
                for next in range(n):
                    if computers[node][next] == 1 and visited[next] == 0:
                        stack.append(next)
                        visited[next] = 1
            answer += 1
    return answer