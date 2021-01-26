#==================================================
#==>      Title: koko-eating-bananas                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/23/2021
#==================================================

"""
https://leetcode-cn.com/problems/koko-eating-bananas/
"""

class Solution:
    def minEatingSpeed(self, piles, H):
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right-left)//2
            if self.canFinish(mid, piles, H):
                right = mid
            else:
                left = mid + 1
        return left
    def canFinish(self, k, piles, H):
        time = 0
        for s in piles:
            if s <= k:
                time += 1
            else:
                temp = 0 if s % k == 0 else 1
                time += s // k + temp
        return time <= H

mat = Solution()
piles = [3,6,7,11]
H = 8
piles = [30,11,23,4,20]
H = 5
mat.minEatingSpeed(piles, H)
