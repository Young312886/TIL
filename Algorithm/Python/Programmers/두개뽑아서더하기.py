def solution(numbers):
    answer = []
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            key = numbers[i]
            adding = numbers[j]
            adding += key
            print(adding)
            if adding not in answer:
                answer.append(adding)
    answer.sort()
    return answer