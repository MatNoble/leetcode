#==================================================
#==>      Title: reverse-string                                 
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/9/2021
#==================================================

"""
https://leetcode-cn.com/problems/reverse-string/
"""

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

string = ["h","e","l","l","o"]
mat = Solution()
mat.reverseString(string)
print(string)
