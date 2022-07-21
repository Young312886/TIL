# 11654

# a = input()

# print(ord(a))

# 11720

# a = int(input())
# b = input()
# result = 0
# for i in b:
#     result += int(i)
# print(result)

# 10809

# a = input()
# alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# for i in alphabet:
#     print(a.find(i), end = " ")
    
# 2675
# t = int(input())
# for i in range(t):
#     a, b= input().split()
#     a = int(a)
#     for i in b:
#         print(i*a, end='')
#     print()
    
# # 1157
# a = input().lower()
# b = list(a)
# c = set(b)
# c = sorted(list(c))
# counting = []
# for i in c:
#     counting.append(b.count(i))
# k = max(counting)
# if counting.count(k) == 1:
#     print(c[counting.index(k)].upper())
# else : 
#     print("?")

# 1152

# a = list(map(str, input().split()))
# print(len(a))

#2908

# a,b = map(str, input().split())
# a1, b1 = int(a[::-1]), int(b[::-1])
# if a1 >= b1 :
#     print(a1)
# else :
#     print(b1)

# # 5622
# a = list(input())
# num_list = [["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],
# ["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y","Z"]]
# result = 0
# for i in a:
#     for idx, j in enumerate(num_list,start = 3):
#         if i in j:
#             result += idx
#         else : continue
# print(result)
 

# 2941

# new_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]
# word = input()
# for i in new_list:
#     word = word.replace(i, "p")
# print(len(word))

t = int(input())
k = [1]*t
for idx,i in enumerate(range(t)):
    word = input()
    single = sorted(list(set(list(word))))
    for j in single:
        counter = word.count(j)
        if counter == 1:
            continue
        else :
            place = word.find(j)
            counter2 = 1
            i = 1
            while True:
                if (place + i) == (len(word)):
                    if counter == counter2:
                        break
                    else :
                        k[idx] = False
                        break
                if word[place] == word[place+i]:
                    i += 1
                    counter2 += 1
                    continue
                else :
                    if counter == counter2:
                        break
                    else :
                        k[idx] =False
                        break
print(sum(k))
        # 1개면 패스
        # 여러개이다. 찾아보도록 / 어 근데 연속되는거 다 찾음 근데 count랑 안 맞음 땡