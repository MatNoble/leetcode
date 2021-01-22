#==================================================
#==>      Title: search-in-rotated-sorted-array
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/21/2021
#==================================================

"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target: return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left  = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1

mat = Solution()
nums = [4,5,6,7,0,1,2]
nums = [1]
# nums = [1, 3]
target = 8
target = 0
mat.search(nums, target)
