def fn_d(n):
    result = 0
    while n > 10:
        divide = n % 10
        n = n // 10
        result += divide
    result += n
    return n
def is_selfnumber(n):
    non_self = list()
    for i in range(n):
        non_self.append(fn_d(n))
    if n in non_self:
        return False
    else :
        return True
    
def count_vowels(words):
    vowels = ['a','e','i','o','u']
    result = 0
    for i in vowels:
        result += words.count(i)
    return result

print(count_vowels('banana'))

def only_square_area(x,y):
    result = 0
    for i in x:
        if i in y:
            result += i**2

    return result
print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
print(32**2+55**2)

def count_blood(blood):
    result = dict()
    for i in blood:
        result[i] += 1

    return result
blood_dict = count_blood(['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB'])
print(blood_dict)