#==================================================
#==>      Title:                                     
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/27/2021
#==================================================

"""
https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
"""

class Solution:
    def findRepeatNumber(self, nums):
        # dict = set()
        # for num in nums:
        #     if num in dict: return num
        #     dict.add(num)
        # return -1
        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            swap(nums, i, nums[i])
        return -1

mat = Solution()
nums = [2, 3, 1, 0, 2, 5, 3]
nums = [0, 1, 2, 3, 2]
mat.findRepeatNumber(nums)
