#==================================================
#==>      Title: 剑指 Offer 10- II. 青蛙跳台阶问题
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/30/2021
#==================================================

"""
https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
"""

class Solution:
    def numWays(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n+1):
            a, b = b, (a+b) % 1000000007
        return a
    def numWaysRecursion(self, n: int) -> int:
        if n <= 1: return 1
        return self.numWaysRecursion(n-1) + self.numWaysRecursion(n-2)

mat = Solution()
n = 2
print(mat.numWays(7))
print(mat.numWaysRecursion(7)) # 栈会溢出

