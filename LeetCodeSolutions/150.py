#==================================================
#==>      Title:                                     
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 
#==================================================

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        # if n < 3: return False
        i = res = 0
        stack = []
        while i<n:
            if tokens[i] == '+':
                tmp = stack.pop()
                res = stack.pop() + tmp
            elif tokens[i] == '-':
                tmp = stack.pop()
                res = stack.pop() - tmp
            elif tokens[i] == '*':
                tmp = stack.pop()
                res = stack.pop() * tmp
            elif tokens[i] == '/':
                tmp = stack.pop()
                res = int(stack.pop() / tmp)
            else:
                res = int(tokens[i])
            stack.append(res)
            i += 1
        return stack[0]

mat = Solution()
tokens = ["2", "1", "+", "3", "*"]
# tokens = ["4", "13", "5", "/", "+"]
# tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tokens = ["18"]
mat.evalRPN(tokens)
