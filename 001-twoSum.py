#==================================================
#==>      Title: Leetcode-001-two-sum                                   
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/6/2021
#==================================================

'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
你可以按任意顺序返回答案。

======================================================
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
======================================================

链接：https://leetcode-cn.com/problems/two-sum
'''

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[i] + nums[j] - target) < 1E-6:
                    return [i, j]
    def twoSum1(self, nums, target):
    	mapping = {}
    	for index, val in enumerate(nums):
    		diff = target - val
    		if diff in mapping:
    			return [index, mapping[diff]]
    		else:
    			mapping[val] = index
    
nums = [2, 4, 7, 10, 9, 16]
target = 12

mat = Solution()
mat.twoSum(nums, target)
mat.twoSum1(nums, target)

