#==================================================
#==>      Title: asteroid-collision                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/15/2021
#==================================================

"""
https://leetcode-cn.com/problems/asteroid-collision/
"""

class Solution:
    def asteroidCollision(self, asteroids):
        n = len(asteroids)
        stack = []
        for i in range(n):
            ast = asteroids[i]
            if ast > 0:
                stack.append(ast)
            else:
                while stack and stack[-1] > 0 and stack[-1] < - ast:
                    stack.pop()
                if len(stack) != 0 and stack[-1] == -ast:
                    stack.pop()
                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(ast)
        return stack

mat = Solution()
a = [5,10,-5]
a = [-2,-1,1,2]
mat.asteroidCollision(a)
