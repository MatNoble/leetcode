#==================================================
#==>      Title: permutations                                   
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/21/2021
#==================================================

"""
https://leetcode-cn.com/problems/permutations/
"""

class Solution:
    def permute(self, nums):
        def backtrack(nums, track):
            if len(nums) == len(track):
                res.append(track[:])
                return
            for temp in nums:
                if temp in track: continue
                track.append(temp)
                backtrack(nums, track)
                track.pop()
        res, track = [], []
        backtrack(nums, track)
        return res

nums = [1, 2, 3]
# nums = []
mat = Solution()
print(mat.permute(nums))
