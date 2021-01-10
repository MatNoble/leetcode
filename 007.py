#==================================================
#==>      Title: Leetcode-007-reverse                                   
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/6/2021
#==================================================

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
https://leetcode-cn.com/problems/reverse-integer/
'''

class Solution:
    def reverse(self, x: int) -> int:
        temp = str(x) if x>0 else str(-x) + '-'
        y = int(temp[::-1])
        return y if abs(y) <= 2**31-1 else 0

mat = Solution()
print(mat.reverse(1450))
print(mat.reverse(7200))

