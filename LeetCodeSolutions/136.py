#==================================================
#==>      Title: 136. 只出现一次的数字
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/22/2021
#==================================================

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # from collections import Counter
        # return sorted(Counter(nums).items(),key=lambda x:x[1])[0][0]
        for num in nums[1:]:
            nums[0] ^= num
        return nums[0]

mat = Solution()
nums = [2,3,2,1,1]
mat.singleNumber(nums)
