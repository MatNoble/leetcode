#==================================================
#==>      Title: 724. 寻找数组的中心索引
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/28/2021
#==================================================

"""
https://leetcode-cn.com/problems/find-pivot-index/
"""

class Solution:
    def pivotIndex(self, nums):
        sum_ = 0
        for val in nums: sum_ += val
        sum_left = 0
        for idx, val in enumerate(nums):
            if 2*sum_left + val == sum_: return idx
            sum_left += val
        return -1

mat = Solution()
nums = [1, 7, 3, 6, 5, 6]
# nums = [1, 2, 3]
nums = [1]
nums = [1, 2]
nums = [1, -1, 1]
mat.pivotIndex(nums)
