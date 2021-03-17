#==================================================
#==>      Title: 05. 替换空格
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/27/2021
#==================================================

"""
https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
"""

class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for val in s:
            if val == ' ':
                res += '%20'
            else:
                res += val
        return res

mat = Solution()
s = "We are happy."
mat.replaceSpace(s)
