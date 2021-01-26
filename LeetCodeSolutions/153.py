#==================================================
#==>      Title: find-minimum-in-rotated-sorted-array
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/22/2021
#==================================================

"""
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] < nums[right]: return nums[left]
            mid = left + (right-left)//2
            if nums[left] <= nums[mid]:
                left = mid+1
            else:
                right = mid
        return nums[left]

mat = Solution()
nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
# nums = [1]
mat.findMin(nums)
