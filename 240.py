#==================================================
#==>      Title: search-a-2d-matrix-ii
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/22/2021
#==================================================

"""
https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
"""

class Solution:
    def searchMatrix(self, matrix, target):
        n, m = len(matrix), len(matrix[0])
        if  n == 0: return True
        i, j = n-1, 0
        while i >= 0 and j < m:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True
        return False

mat = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 20

mat.searchMatrix(matrix, target)
