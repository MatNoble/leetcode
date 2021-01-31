#==================================================
#==>      Title: 989. 数组形式的整数加法
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/31/2021
#==================================================

"""
https://leetcode-cn.com/problems/add-to-array-form-of-integer/
"""

from typing import List
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        i, n, count = -1, len(A), 0
        while -i < n+1 and (K or count):
            temp = A[i] + count + K % 10
            A[i], count = temp % 10, temp // 10
            K = K // 10
            i -= 1
        while K:
            temp = count + K % 10
            A.insert(0, temp % 10)
            count = temp // 10
            K = K // 10
        return A if count == 0 else [count]+A

mat = Solution()
A = [1,1]
K = 11
# K = 9
K = 11999
mat.addToArrayForm(A, K)
