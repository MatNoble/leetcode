#==================================================
#==>      Title: 498. 对角线遍历
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/30/2021
#==================================================

"""
https://leetcode-cn.com/problems/diagonal-traverse/
"""

from typing import List
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0: return []
        flag = 1
        i = j = 0
        n = len(matrix[0])
        res = [matrix[0][0]]
        while i < m and j < n:
            if flag == 1:
                if j < n-1: 
                    j += 1
                else:
                    i += 1
                while 0 <= i < m and 0 <= j < n:
                    res.append(matrix[i][j])
                    i += 1
                    j -= 1
                i -= 1
                j += 1
                flag = 0
            else:
                if i < m-1:
                    i += 1
                else:
                    j += 1
                while 0 <= i < m and 0 <= j < n:
                    res.append(matrix[i][j])
                    i -= 1
                    j += 1
                i += 1
                j -= 1
                flag = 1
        return res

mat = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

matrix = [
 [ 1, 2, 3, 4 ],
 [ 5, 6, 7, 8 ],
 [ 9, 10, 11, 12 ]
]

# matrix = []
mat.findDiagonalOrder(matrix)
