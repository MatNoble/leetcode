#==================================================
#==>      Title: subsets                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/18/2021
#==================================================

"""
https://leetcode-cn.com/problems/subsets/
"""

import copy

class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in range(len(nums)):
            k, ress = nums[i], copy.deepcopy(res)
            for j in range(len(res)): ress[j].append(k)
            res += ress
        return res

    def subsets_recursion(self, nums):
        if not nums: return [[]]
        res = self.subsets_recursion(nums[:-1])
        k, ress = nums[-1], copy.deepcopy(res)
        for i in range(len(ress)): ress[i].append(k)
        return res + ress

nums = [1, 2, 3]
mat = Solution()
mat.subsets(nums)
# mat.subsets_recursion(nums)
