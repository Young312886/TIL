import math
def solution(brown, yellow):
    
    
    b = (brown+4)/4 + math.sqrt(((brown+4)/2)**2 - 4*(yellow+brown))/2
    a = (yellow+brown)/b
    answer = [b,a]
    return answer