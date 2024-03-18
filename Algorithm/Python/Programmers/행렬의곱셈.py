def solution(arr1, arr2):
    
    a, b = len(arr1), len(arr1[0])
    c, d = len(arr2), len(arr2[0])
    answer = [[0] * d for _ in range(a)]
    for i in range(a):
        single = 0
        left = arr1[i]
        for j in range(d):
            right = []
            for k in range(b):
                answer[i][j] += left[k] * arr2[k][j]
                # print(arr2[k][j])
            
    return answer