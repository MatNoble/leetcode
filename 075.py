#==================================================
#==>      Title: sort-colors                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/25/2021
#==================================================

"""
https://leetcode-cn.com/problems/sort-colors/
"""

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        if n == 1: return
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        i, zero, two = 0, -1, n-1
        while i <= two:
            if nums[i] == 0:
                zero += 1
                swap(nums, i, zero)
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums, i, two)
                two -= 1

mat = Solution()
nums = [2,0,2,1,1,2]
nums = [2,0,1]
mat.sortColors(nums)
print(nums)
