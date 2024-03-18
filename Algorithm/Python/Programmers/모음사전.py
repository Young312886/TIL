
dictionary = []
idx = ['A', 'E', 'I', 'O', 'U']
def permut (base):
    if len(base) == 5:
        return
    for i in range(5):
        dictionary.append(base + idx[i])
        permut(base + idx[i])
permut("")
# print(dictionary)
def solution(words):

    return dictionary.index(words) + 1