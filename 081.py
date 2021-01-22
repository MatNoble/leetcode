#==================================================
#==>      Title: search-in-rotated-sorted-array-ii
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/22/2021
#==================================================

"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/
"""

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target: return True
            while left < mid and nums[left] == nums[mid]: left += 1
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return False

mat = Solution()
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2

nums = [2,5,6,0,0,1,2]
target = 0

nums = [2,5,6,0,0,1,2]
target = 3
mat.search(nums, target)
