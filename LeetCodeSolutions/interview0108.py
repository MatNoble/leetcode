#==================================================
#==>      Title: 面试题 01.08. 零矩阵
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/30/2021
#==================================================

"""
https://leetcode-cn.com/problems/zero-matrix-lcci/
"""

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        I, J = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    I.add(i)
                    J.add(j)
        for i in range(m):
            for j in range(n):
                if (i in I) or (j in J): matrix[i][j] = 0

matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

# matrix = [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]

mat = Solution()
mat.setZeroes(matrix)
print(matrix)
print(type(matrix))
