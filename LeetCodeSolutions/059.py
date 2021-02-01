#==================================================
#==>      Title: 59. 螺旋矩阵 II
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/1/2021
#==================================================

"""
https://leetcode-cn.com/problems/spiral-matrix-ii/
"""

from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i = j = 0
        k = c = 1
        res = [[0]*n for i in range(n)]
        while k < n*n:
            while j < n-c:
                res[i][j] = k
                k += 1
                j += 1
            while i < n-c:
                res[i][j] = k
                k += 1
                i += 1
            while j > c-1:
                res[i][j] = k
                k += 1
                j -= 1
            while i > c-1:
                res[i][j] = k
                k += 1
                i -= 1
            i += 1
            j += 1
            c += 1
        if k == n*n: res[i][i] = k
        return res

mat = Solution()
n = 7
# n = 1
mat.generateMatrix(n)
