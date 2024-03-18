def solution(routes):
    answer = 0
    for route in routes:
        route.sort()
    routes.sort(key = lambda x : x[1])
    cam = -300001
    for go, out in routes:
        if go > cam:
            answer += 1
            cam = out
    return answer