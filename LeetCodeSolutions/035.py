#==================================================
#==>      Title: 35. 搜索插入位置
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/29/2021
#==================================================

"""
https://leetcode-cn.com/problems/search-insert-position/
"""

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]: return 0
        if target > nums[-1]: return len(nums)

        i, j = 0, len(nums)-1
        while i < j - 1:
            mid = i + (j-i) // 2
            if nums[mid] == target: return mid
            if nums[mid] > target:
                j = mid
            else:
                i = mid
        return i if nums[i] == target else j

mat = Solution()
nums = [1,3,5,6]
target = 5

# nums = [1,3,5,6]
# target = 2

# nums = [1,3,5,6]
# target = 7

nums = [1,3,5,6]
target = 0

nums = [1, 3]
target = 1
mat.searchInsert(nums, target)
