k = (1,2)
print(type(k))
p = []
p.append(k)
print(p)
for i in range(0,8,2):
    p.append((i,i+1))
print(p)

p = [1,2,3]
j = tuple(p)
print(j, type(j))