#==================================================
#==>      Title: 剑指 Offer 03. 数组中重复的数字                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/27/2021
#==================================================

"""
https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
"""

from collections import Counter 
class Solution:
    def findRepeatNumber(self, nums):
        # 计数法
        # return Counter(nums).most_common(1)[0][0]

        # 哈希表
        # dict = set()
        # for num in nums:
        #     if num in dict: return num
        #     dict.add(num)
        # return -1

        # 原地置换  环
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == i: 
                i += 1
                continue
            if nums[nums[i]] == nums[i]: 
                return nums[i] # 环入口
            j = nums[i] # 归位
            nums[i], nums[j] = nums[j], nums[i]
        return -1

mat = Solution()
nums = [2, 3, 1, 0, 2, 5, 3]
nums = [0, 1, 2, 3, 2]
mat.findRepeatNumber(nums)
