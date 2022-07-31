for i in range(10):
    target = int(input())
    boxes = list(map(int, input().split()))
    n = 0
    while n < target:
        highest = max(boxes)
        lowest = min(boxes)
        if highest - lowest <= 1:
            result = highest - lowest
            break
        boxes[boxes.index(highest)] = highest - 1
        boxes[boxes.index(lowest)] = lowest + 1
        n += 1
    result = max(boxes) - min(boxes)
    print(f"#{i+1} {result}") 

# a = [1,2,3,4,5]
# j = a.index(min(a))

# a[j] = min(a)-1
# print(a)