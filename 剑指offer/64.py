#==================================================
#==>      Title: 剑指 Offer 64. 求1+2+…+n
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/30/2021
#==================================================

"""
https://leetcode-cn.com/problems/qiu-12n-lcof/
and 操作如果结果为真，返回最后一个表达式的值，
 or 操作如果结果为真，返回第一个结果为真的表达式的值
"""

class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n+self.sumNums(n-1))

mat = Solution()
mat.sumNums(3)
