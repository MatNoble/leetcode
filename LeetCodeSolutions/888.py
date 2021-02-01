#==================================================
#==>      Title: 888. 公平的糖果棒交换
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/1/2021
#==================================================

"""
https://leetcode-cn.com/problems/fair-candy-swap/
"""

from typing import List
import collections
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        # sumA = sumB = 0
        # for val in A: sumA += val
        # for val in B: sumB += val
        # if len(A) <= len(B):
        #     dic = collections.Counter(B)
        #     diff = (sumA - sumB) // 2
        #     for a in A: 
        #         if a - diff in dic: 
        #             return [a, a-diff]
        # else:
        #     dic = collections.Counter(A)
        #     diff = (sumB - sumA) // 2
        #     for b in B:
        #         if b - diff in dic: 
        #             return [b-diff, b]

        sumA = sumB = 0
        set_ = set()
        for val in A: sumA += val
        for val in B:
            sumB += val
            set_.add(val)
        diff = (sumA - sumB)//2
        for a in A:
            if a-diff in set_:
                return [a, a-diff]


mat = Solution()
A = [1, 2, 3, 5]
B = [2, 3]

B = [1,1,1,1,1,1,1,12]
A = [5]

A = [1,1,1,1,1,1,1,12]
B = [5]
mat.fairCandySwap(A, B)
