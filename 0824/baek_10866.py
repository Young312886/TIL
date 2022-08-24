class Deque:
    def __init__(self):
        self.stack = []

    def push_back(self,k):
        self.stack.append(k)

    def push_front(self,k):
        self.stack = [k] + self.stack

    def front(self):
        if self.stack:
            return self.stack[0]
        else:
            return -1
    def back(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
    def size(self):
        return len(self.stack)

    def empty(self):
        return 0 if self.stack else 1
    def pop_front(self):
        if self.stack:
            return self.stack.pop(0)
        else:
            return -1
    def pop_back(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1


answer = Deque()
for _ in range(int(input())):
    p = input()
    if p == "front":
        print(answer.front())
    elif p == "back":
        print(answer.back())
    elif p == "size":
        print(answer.size())
    elif p == "empty":
        print(answer.empty())
    elif p == "pop_front":
        print(answer.pop_front())
    elif p == "pop_back":
        print(answer.pop_back())
    else:
        k,j = map(str, p.split())
        if k == "push_back":
            answer.push_back(j)
        elif k == "push_front":
            answer.push_front(j)