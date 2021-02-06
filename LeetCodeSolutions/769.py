#==================================================
#==>      Title: 769. 最多能完成排序的块
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/6/2021
#==================================================

"""
https://leetcode-cn.com/problems/max-chunks-to-make-sorted/
"""

from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        k = 0
        max_ = arr[0]
        for idx, val in enumerate(arr):
            max_ = max(max_, val)
            if max_ <= idx: k += 1
        return k

mat = Solution()
arr = [4,3,2,1,0]
arr = [1,0,2,3,4]
mat.maxChunksToSorted(arr)
