#==================================================
#==>      Title: 394. 字符串解码
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/2/2021
#==================================================

"""
https://leetcode-cn.com/problems/decode-string/
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res

# 参考：https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/

mat = Solution()
s = "3[a]2[bc]"
s = "abc3[cd]xyz"
# s = "2[abc]3[cd]ef"
# s = "3[a2[c]]"
s = "2[2[2[ab]]]"
mat.decodeString(s)
