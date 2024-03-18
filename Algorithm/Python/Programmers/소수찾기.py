visited = [0] * 10000000
def is_prime(n):
    if visited[n] == 1:
        return False
    visited[n] = 1
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

from itertools import permutations
def solution(numbers):
    bank = list(numbers)
    answer = 0
    for i in range(len(numbers)+1):
        numbers = list(permutations(bank,i))
        for single_num in numbers:
            if not single_num:
                continue
            num = int(''.join(single_num))
            answer += is_prime(num)
    return answer