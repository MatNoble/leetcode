#==================================================
#==>      Title: 209. 长度最小的子数组
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/9/2021
#==================================================

"""
https://leetcode-cn.com/problems/minimum-size-subarray-sum/
"""

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        n = len(nums)
        res = n+1
        sum_ = 0
        flag = 0
        while j < n:
            while j < n and sum_ < target:
                sum_ += nums[j]
                j += 1
            while sum_ >= target:
                res = min(res, j-i)
                sum_ -= nums[i]
                i += 1
        return res if res!=n+1 else 0

mat = Solution()
target = 7
nums = [7,2,3,1,2,4,3]

# target = 11
# nums = [1,1,1,1,1,1,1,1]
mat.minSubArrayLen(target, nums)
