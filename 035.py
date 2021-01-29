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
        left, right = 0, len(nums)-1
        while left < right-1:
            mid = left + (right-left+1)//2
            if nums[mid] < target:
                left = mid
            elif target < nums[mid]:
                right = mid
            else:
                return mid
        if target <= nums[left]:
            return left
        elif nums[right] < target:
            return right + 1
        else:
            return right

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
