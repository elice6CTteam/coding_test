nums = [2,2,2,3,3,3]

def solution(nums):
    l = len(nums)/ 2
    s = len(set(nums))
    
    if l > s :
        return s
    else:
        return l
    
print(solution(nums))