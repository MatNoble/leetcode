#==================================================
#==>      Title: 859. 亲密字符串
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/1/2021
#==================================================

"""
https://leetcode-cn.com/problems/buddy-strings/
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        n, m = len(A), len(B)
        if n != m: return False
        if A == B:
            C = set()
            for a in A:
                if a in C: return True
                C.add(a)
            return False
        else:
            C = []
            for i in range(n):
                if A[i] != B[i]:
                    C.append([A[i], B[i]])
                if len(C) >=3: return False
            return len(C) == 2 and C[0] == C[-1][::-1]

mat = Solution()
A = 'acb'
B = 'abc'
A = 'aa'
B = 'aa'
mat.buddyStrings(A, B)
