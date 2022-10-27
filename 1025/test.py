def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    def binary(first, second):
        if first < second:
            n1 = numbers[first]
            n2 = numbers[second]
            if n1 + n2 == target:
                print(first, second)
                return first+1
            
            elif n1 + n2 > target:
                
                if first +1 == second:
                    if first >= 1:
                        return binary(first-1,second)
                else:
                    return binary(first, second-1)
                    
            elif n1 + n2 < target:
                
                if second == len(numbers) -1:
                    return binary(first + 1, second)
                return binary(first, second + 1)
                    
        else:
            return('wrong')
    return binary(0,1)

print(twoSum([2,3,4],6))