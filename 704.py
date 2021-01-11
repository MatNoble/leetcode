#==================================================
#==>      Title: binary-search
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/11/2021
#==================================================

"""
https://leetcode-cn.com/problems/binary-search/
"""

class Solution:
    def search(self, nums, target):
        i, j = 0, len(nums)-1
        while i <= j:
            mid = i + (j-i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1

nums = [-1,0,3,5,9,12]
target = 9 # 4

# nums = [-1,0,3,5,9,12]
# target = 2 # -1

mat = Solution()
mat.search(nums, target)
