a = [5,2,5,7,2,1,7]
a1 = sorted(a)
print(a1)

a = [3,6,8,3]
b = [1,2,3,4]
c1 = a.extend(b)
print(a)
c2 = a.append(b)
print(a)
print(c1,c2)

a = [1,2,3,4,5]
b = a
a[2] = 5
print(a)
print(b)
print(id(a))
print(id(b))

def duplicated_letters(words):
  dick = dict()
  result = []
  for i in words:
    if i in dick:
      dick[i] = dick[i] + 1
    else :
      dick[i] = 1
  for key,value in dick.items():
    if value >= 2:
      result.append(key)
  print(result)
  return result


duplicated_letters('apple') 
duplicated_letters('banana') 

def low_and_up(word):
  result = list(word)
  for i in range(1,len(result),2):
    result[i] = result[i].upper()
  word_end = "".join(result)
  return word_end
low_and_up('apple')

def lonely(nums):
    result = []
    result.append(nums[0])
    for i in nums:
        if result[-1] == i:
            continue
        else : 
            result.append(i)
    print(result)
    return result
lonely([1,1,3,3,0,1,1])
