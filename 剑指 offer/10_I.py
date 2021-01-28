#==================================================
#==>      Title: 剑指 Offer 10- I. 斐波那契数列
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/28/2021
#==================================================

"""
https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
"""

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, (a + b) % 1000000007
        return a

mat = Solution()
mat.fib(37)
