#==================================================
#==>      Title:                                     
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 
#==================================================

"""
https://leetcode-cn.com/problems/move-zeroes/submissions/
"""

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

mat = Solution()
nums = [0,1,0,3,12]
nums_ = nums[:]
mat.moveZeroes(nums_)

print(f'before: {nums}')
print(f' after: {nums_}')
