#==================================================
#==>      Title: next-greater-element-ii
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/15/2021
#==================================================

"""
https://leetcode-cn.com/problems/next-greater-element-ii/
"""

class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2*n-1, -1, -1):
            while len(stack) != 0 and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            if len(stack) != 0:
                res[i % n] = nums[stack[-1]]
            stack.append(i % n)
        return res

nums = [1,2,1]
mat = Solution()
mat.nextGreaterElements(nums)
