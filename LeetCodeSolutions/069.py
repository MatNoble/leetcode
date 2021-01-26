#==================================================
#==>      Title: sqrtx
#==>     Author: Zhang Zhen
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/11/2021
#==================================================

"""
https://leetcode-cn.com/problems/sqrtx/
"""

class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0  
        i, j = 1, x // 2 + 1
        while i < j:
            mid = i + (j-i+1) // 2
            if mid > x/mid:
                j = mid - 1
            else: 
                i = mid
        return i

mat = Solution()

x = 2147395599
print(mat.mySqrt(x))
print(int(sqrt(x)))


from math import sqrt

y, z = [], []
for x in range(10):
    y.append(mat.mySqrt(x))
    z.append(int(sqrt(x)))
print(y)
print(z)
