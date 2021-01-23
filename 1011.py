#==================================================
#==>      Title: capacity-to-ship-packages-within-d-days
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/23/2021
#==================================================

"""
https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/
"""

class Solution:
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left)//2
            if self.canFinish(mid, weights, D):
                right = mid
            else:
                left = mid + 1
        return left
    def canFinish(self, k, weights, D):
        times, sums = 1, 0
        for val in weights:
            sums += val
            if sums > k:
                sums = val
                times += 1
        return times <= D

mat = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]
D = 5 # 15
# weights = [3,2,2,4,1,4]
# D = 3 # 6
# weights = [1,2,3,1,1]
# D = 4 # 3
mat.shipWithinDays(weights, D)
# mat.canFinish(15, weights, D)
