#==================================================
#==>      Title: 768. 最多能完成排序的块 II
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/6/2021
#==================================================

"""
https://leetcode-cn.com/problems/max-chunks-to-make-sorted-ii/

题解：
https://matnoble.me/dsa/basic/array-stack-queue/#768-最多能完成排序的块-ii
"""

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for val in arr:
            if stack and val < stack[-1]:
                head = stack.pop()
                while stack and val < stack[-1]: stack.pop()
                stack.append(head)
            else:
                stack.append(val)
        return len(stack)

mat = Solution()
arr = [2,1,3,4,4]
mat.maxChunksToSorted(arr)
