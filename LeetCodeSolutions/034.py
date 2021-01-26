#==================================================
#==>      Title: find-first-and-last-position-of-element-in-sorted-array                                 
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/10/2021
#==================================================

"""
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

class Solution:
    # Two Pointers
    def searchRange_TP(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == target and nums[j] == target:
                return [i, j]
            if nums[i] < target:
                i += 1
            if nums[j] > target:
                j -= 1
        return [-1, -1]

    # Binary Search
    def searchRange_BS(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j-i) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        if nums[j] != target:
            return [-1, -1]
        k = i
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j-i+1) // 2
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
        return [k, i]

nums = [5,7,7,8,8,10]
target = 8
# target = 6

# nums = []
# target = 0

# nums = [1]
# target = 1

# nums = [2, 2]
# target = 3

mat = Solution()
mat.searchRange_TP(nums, target)
