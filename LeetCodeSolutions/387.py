#==================================================
#==>      Title: first-unique-character-in-a-string
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/20/2021
#==================================================

"""
https://leetcode-cn.com/problems/first-unique-character-in-a-string/
"""

import collections

class Solution:
    def firstUniqChar(self, s):
        # hashMap = {}
        # for c in s: hashMap[c] = hashMap.get(c,0) + 1
        hashMap = collections.Counter(s)
        for i, c in enumerate(s):
            if hashMap[c] == 1: return i
        return -1

s = "loveleetcode"
# s = "z"
# s = ""
# s = "cc"
# s = "aadadaad"
mat = Solution()
mat.firstUniqChar(s)
