#==================================================
#==>      Title: shortest-distance-to-a-character                           
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/27/2021
#==================================================

"""
https://leetcode-cn.com/problems/shortest-distance-to-a-character/
"""

from typing import List
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        res = [n]*n
        # first loop
        i = 0
        while S[i] != C[0]: i += 1
        while i < n:
            res[i] = 0 if S[i] == C[0] else res[i-1]+1
            i += 1
        # second loop
        i -= 2
        while i > -1:
            if res[i+1]+1 < res[i]: res[i] = res[i+1]+1 
            i -= 1
        return res

mat = Solution()
S = "loveleetcode"
C = 'e'

# S = "aaba"
# C = "b"
mat.shortestToChar(S, C)
