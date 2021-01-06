#==================================================
#==>      Title: Leetcode-009-isPlindrome                                 
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/6/2021
#==================================================

'''
判断一个整数是否是回文数。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
你能不将整数转为字符串来解决这个问题吗？
======================================================
输入: 121
输出: true

输入: -121
输出: false
解释: 从左向右读, 为 -121 。从右向左读, 为 121- 。因此它不是一个回文数。
======================================================
链接：https://leetcode-cn.com/problems/palindrome-number/
'''

class Solution:
    def isPlindrome(self, x: int) -> bool:
        if x <  0:
            return False
        else:
            y = str(x)[::-1]
            return True if str(x) == y else False

mat = Solution()
mat.isPlindrome(-323)
# mat.isPlindrome(424)
