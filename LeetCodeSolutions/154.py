#==================================================
#==>      Title: 154. 寻找旋转排序数组中的最小值 II
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/31/2021
#==================================================

"""
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            while left < mid and nums[left] == nums[mid]: left += 1
            if nums[left] < nums[right]: return nums[left]
            if nums[left] <= nums[mid]:
                left = mid+1
            else:
                right = mid
        return nums[left]

mat = Solution()
nums = [2, 0, 2, 2]
nums = [1, 2, 3]
nums = [1]
nums = [2, 0, 2, 2, 2, 2, 2]
mat.findMin(nums)
