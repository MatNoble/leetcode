#==================================================
#==>      Title: daily-temperatures                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/15/2021
#==================================================

"""
https://leetcode-cn.com/problems/daily-temperatures/
"""

class Solution:
    ## 前
    def dailyTemperatures(self, T):
        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:    
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res

    ## 后
    def dailyTemperatures_1(self, T):
        res = [0] * len(T)
        stack = []
        # for i in  reversed(range(len(T))):
        for i in  range(len(T)-1, -1, -1):    
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if len(stack) != 0:
                res[i] = stack[-1] - i
            stack.append(i)
        return res  

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
mat = Solution()
print(mat.dailyTemperatures(temperatures))
print(mat.dailyTemperatures_1(temperatures))
