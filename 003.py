#==================================================
#==>      Title: longest-substring-without-repeating-characters
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/12/2021
#==================================================

"""
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        i, cnt = 0, 0
        HashMap = {}
        for idx, val in enumerate(s):
            if HashMap.get(val): i = max(HashMap.get(val), i)
            HashMap[val] = idx + 1
            cnt = max(cnt, idx-i+1)
        return cnt

s = 'abcabcbb'
s = 'pwwkew'
s = 'ewwkea'

mat = Solution()
mat.lengthOfLongestSubstring(s)
