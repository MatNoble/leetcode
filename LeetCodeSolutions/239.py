#==================================================
#==>      Title: sliding-window-maximum
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/26/2021
#==================================================

"""
https://leetcode-cn.com/problems/sliding-window-maximum/
"""

import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        for val in nums[:k]:
            while d and d[-1] < val: d.pop()
            d.append(val)
        res = [d[0]]
        for i in range(k, len(nums)):
            if nums[i-k] == d[0]: d.popleft()
            while d and d[-1] < nums[i]: d.pop()
            d.append(nums[i])
            res.append(d[0])
        return res

mat = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3

# nums = [1]
# k = 1

# nums = [1,-1]
# k = 1

# nums = [9,11]
# k = 2

# nums = [4,-2]
# k = 2

nums = [1,3,1,2,0,5]
k = 3

# nums = [-7,-8,7,5,7,1,6,0]
# k = 4

mat.maxSlidingWindow(nums, k)
