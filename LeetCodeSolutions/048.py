#==================================================
#==>      Title: 48. 旋转图像
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/29/2021
#==================================================

"""
https://leetcode-cn.com/problems/rotate-image/
"""

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for j in range(n//2):
            for i in range(n):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

mat = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1,2],[3,4]]
mat.rotate(matrix)
print(matrix)
