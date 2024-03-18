def solution(numbers, target):
    global answer
    answer = 0
    n = len(numbers)
    def bfs(stack, position):
        global answer
        if position == n:
            if stack == target:
                answer += 1
            else:
                return
        else:
            bfs(stack + numbers[position], position + 1)
            bfs(stack - numbers[position], position + 1)
    bfs(0, 0)
    return answer