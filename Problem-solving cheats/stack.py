#==================================================
#==>      Title: Stack
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/15/2021
#==================================================

"""
Next Greater Element
 in: [2,1,2,4,3]
out: [4,2,4,-1,-1]
"""

def nextGreaterElement(nums):
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        while len(stack) != 0 and nums[i] >= nums[stack[-1]]:
            stack.pop()
        if len(stack) != 0:
            res[i] = nums[stack[-1]]
        stack.append(i)
    return res

"""
循环数组
 in: [2,1,2,4,3]
out: [4,2,4,-1,4]
"""

def nextGreaterElementCircle(nums):
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(2*n-1, -1, -1):
        while len(stack) != 0 and nums[i % n] >= nums[stack[-1]]:
            stack.pop()
        if len(stack) != 0:
            res[i % n] = nums[stack[-1]]
        stack.append(i % n)
    return res

nums = [2,1,2,4,3]

# Next Greater Element
print(nextGreaterElement(nums))

# 循环数组
print(nextGreaterElementCircle(nums))
