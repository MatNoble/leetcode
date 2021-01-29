#==================================================
#==>      Title: 119. 杨辉三角 I
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/29/2021
#==================================================

"""
https://leetcode-cn.com/problems/pascals-triangle-i/
"""

class Solution:
    def addList(self, a, b):
        return [i+j for i, j in zip(a, b)]
    def generateRecursion(self, numRows):
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        res = self.generateRecursion(numRows-1)
        ress = [1] + self.addList(res[-1][:-1], res[-1][1:]) + [1]
        return res + [ress]
    def generate(self, numRows):
        if numRows == 0: return []
        res = [[1]]
        for i in range(numRows-1):
            ress = [1] + self.addList(res[-1][:-1], res[-1][1:]) + [1]
            res += [ress]
        return res
mat = Solution()
mat.generateRecursion(5)
mat.generate(5)
