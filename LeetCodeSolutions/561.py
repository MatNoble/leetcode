#==================================================
#==>      Title: 561. 数组拆分 I
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/1/2021
#==================================================

"""
https://leetcode-cn.com/problems/array-partition-i/
"""

from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2
        i = sum_ = 0
        for i in range(n):
            j = 2*i
            sum_ += nums[j]
        return sum_

mat = Solution()
nums = [1,4,3,2]
mat.arrayPairSum(nums)
