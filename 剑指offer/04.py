#==================================================
#==>      Title: Offer 04. 二维数组中的查找
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/27/2021
#==================================================

"""
https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
"""

class Solution:
    def findNumberIn2DArray(self, matrix, target):
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        i, j = m-1, 0
        while i >= 0 and j < n:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True
        return False

mat = Solution()
matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
# matrix = []
target = 5
# target = 20
mat.findNumberIn2DArray(matrix, target)
