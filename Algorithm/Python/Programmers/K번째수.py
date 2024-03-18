def solution(array, commands):
    answer = []
    for x,y, idx in commands:
        answer.append(sorted(array[x-1:y])[idx-1])
    return answer