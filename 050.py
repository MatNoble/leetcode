#==================================================
#==>      Title: powx-n
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/11/2021
#==================================================

"""
https://leetcode-cn.com/problems/powx-n/
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        res = 1.0
        if n < 0: x, n = 1.0 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res

    def myPowR(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        def my_pow(x, n):
            if n == 0: return 1.0
            res = my_pow(abs(x), abs(n) // 2)
            res *= res
            if abs(n) % 2: res *= x
            return res
        res = my_pow(x, n)
        return 1/res if n<0 else res

x = 0
x = -3
n = 1
n = 5
mat = Solution()
print(mat.myPow(x, n))
print(mat.myPowR(x, n))
