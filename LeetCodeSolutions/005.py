#==================================================
#==>      Title: longest-palindromic-substring
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/20/2021
#==================================================

"""
https://leetcode-cn.com/problems/longest-palindromic-substring/
"""

class Solution:
    def longestPalindrome(self, s):
        def palindrome(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                    i -= 1
                    j += 1
            return s[i+1: j]
        res = ''
        for i in range(len(s)):
            s1 = palindrome(s, i, i)
            s2 = palindrome(s, i, i+1)
            if len(s1) > len(res): res = s1
            if len(s2) > len(res): res = s2
        return res

s = "cbbd"
s = "aba"
# s = "aaa"
s = "aaaa"
# s = ""
# s = "a"
mat = Solution()
mat.longestPalindrome(s)
