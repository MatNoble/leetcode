#==================================================
#==>      Title: subarray-sum-equals-k
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/12/2021
#==================================================

"""
https://leetcode-cn.com/problems/subarray-sum-equals-k/
"""

class Solution:
    def subarraySum(self, nums, k):
        HashMap = {0:1}
        sum_, cnt = 0, 0
        for x in nums:
            sum_ += x
            temp = HashMap.get(sum_ - k)
            if temp is not None:
                cnt += temp
            HashMap[sum_] = HashMap.get(sum_) + 1 if HashMap.get(sum_) is not None else 1 
        return cnt

nums = [3, 4, 7, 2, -3, 1, 4, 2]
nums = [3, 4, 7, -7]
k = 7
mat = Solution()
mat.subarraySum(nums, k)
