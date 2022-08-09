def sorting(x):
    y = x.split(',')
    for idx, i in enumerate(y):
        i = i.lower()
        if i[:6] == 'rotten':
            i = i[6:]
        y[idx] = i
    return y

names = "apple,rottenapple,banana,Rottenbanana"
sorting(names)
# 계산기 파일 만들기
def add(x,y):
    result = x+y
    return result
def sub(x,y):
    result = x - y
    return result
def mul(x,y):
    result = x*y
    return result
def div(x,y):
    if y == 0:
        return "0으로 나눌수 없습니다"
    else :
        return x/y

# count  없이 글자 수 세기
def count_vowels(x):
    vowels = 'aeiou'
    result = 0
    for vowels in vowels:
        for j in x:
            if vowels == j:
                result += 1

    return result

# 유일 숫자 들의 합
def sum_of_repeat_number(k):
    num_dict = dict()
    result = 0
    for i in k:
        if i in num_dict.keys():
            num_dict[i] = num_dict[i]
        else:
            num_dict[i] = 1
    for j in num_dict:
        if num_dict[j] == 1:
            result += j
    return result

# 부정어 만들기
def negative(words):
    dick = {"b":"im","m":"im","p":"im","l":"il","r":"ir"}
    result = []
    for i in words: 
        try :
            k = i[0]
            change = dick[k] + i
            result.append(change)
        except:
            change = "in" + i
            result.append(change)
            
    result.sort()
    return result

words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}
print(negative(words_dict))

def mass_percent():
    water_list = []
    n = 1
    while n < 5:
        a = input(f"{n}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오 :")
        if a != "Done":
            water_list.append(list(a.split()))
            n+=1
            continue
        else:
            break
    salt = 0
    water = 0
    for i in water_list:
        x , y = int(i[0][:-1]), int(i[1][:-1])
        salt += x * y
        water += y
    print(f"{x/y*100:.1f}% {y:.1f}g")

mass_percent()

# 애너그램 단위 그루핑

def group_anarams(words):
    result = []
    group_dic = dict()
    for i in words:
        anagram = sorted(list(i))
        if anagram in group_dic:
            group_dic[anagram] = group_dic[anagram].append(i)
        else :
            group_dic[anagram] = [i]
    for j in group_dic.values():
        result.append(j)
    return result
# new = group_anarams(['eat','ate','tea','nat','tan','bat'])
# print(new)