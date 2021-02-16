#==================================================
#==>      Title: 剑指 Offer 53 - II. 0～n-1中缺失的数字
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/15/2021
#==================================================

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.insert(0, -1)
        nums.append(len(nums))
        left, right = 0, len(nums)-1
        while left < right-1:
            mid = left + (right-left)//2
            if nums[mid] == (nums[right] + nums[left] - 1) //2:
                left = mid
            else:
                right = mid
        return (nums[left] + nums[right]) // 2

mat = Solution()
nums = [0,1,2,3,4,5,6,7,9]
nums = [0]
nums = [1]
mat.missingNumber(nums)
