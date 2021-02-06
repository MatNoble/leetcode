#==================================================
#==>      Title: 946. 验证栈序列
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/6/2021
#==================================================

"""
https://leetcode-cn.com/problems/validate-stack-sequences/
"""

from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        i = j = 0
        while i < n:
            while i < n and pushed[i] != popped[j]: 
                stack.append(pushed[i])
                i += 1
            i += 1
            j += 1
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            if j < n and popped[j] in stack: return False # 提前结束
        return True if len(stack)==0 else False

mat = Solution()
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]

pushed = [1,2,3,4,5,6,7]
popped = [1,2,5,3,6,7,4]
mat.validateStackSequences(pushed, popped)
