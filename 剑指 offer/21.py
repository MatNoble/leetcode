#==================================================
#==>      Title: 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/2/2021
#==================================================

"""
https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
"""

from typing import List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

mat = Solution()
nums = [1,2,3,4]
mat.exchange(nums)
