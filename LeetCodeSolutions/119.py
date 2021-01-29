#==================================================
#==>      Title: 119. 杨辉三角 II
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/29/2021
#==================================================

"""
https://leetcode-cn.com/problems/pascals-triangle-ii/
"""

class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        res = self.getRow(rowIndex-1)
        return [1] + self.addList(res[:-1], res[1:]) + [1]
    def addList(self, a, b):
        return [i+j for i, j in zip(a, b)]

mat = Solution()
mat.getRow(3)
