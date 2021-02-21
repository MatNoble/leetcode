#==================================================
#==>      Title: 53. 最大子序和
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/21/2021
#==================================================

"""
https://leetcode-cn.com/problems/maximum-subarray/submissions/
"""

from typing import List

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         sum_ = 0
#         res = max(nums)
#         if res <= 0: return res
#         for num in nums:
#             sum_ += num
#             res = max(res, sum_)
#             if sum_ <= 0: sum_ = 0
#         return res

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)

mat = Solution()
nums = [-1, -2]
mat.maxSubArray(nums)
