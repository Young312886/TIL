import sys
sys.stdin = open('projects/TIL/0808/sample.txt','r')
a = int(input())

print(a)

k = [1,1,1,2,3]
if [1,1,1] in k:
    print(True)
else : 
    print(False)