#==================================================
#==>      Title: 剑指 Offer 57 - II. 和为s的连续正数序列
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/21/2021
#==================================================

"""
https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
"""

from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 滑动窗口
        i = j = 1
        sum_, res = 0, []
        while i <= target // 2: # 左窗口不超过 target 的一半
            while sum_ < target:   # 扩大窗口, 右窗口右移 
                sum_ += j
                j += 1
            while sum_ >= target:   # 收缩窗口, 左窗口右移
                if sum_ == target:  # 添加结果
                    res.append([val for val in range(i, j)])
                sum_ -= i
                i += 1
        return res

mat = Solution()
target = 9
target = 15
mat.findContinuousSequence(target)
