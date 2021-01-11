#==================================================
#==>      Title: single-element-in-a-sorted-array
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/11/2021
#==================================================

"""
https://leetcode-cn.com/problems/single-element-in-a-sorted-array/
"""

class Solution:
    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        i, j = 0, len(nums) - 1
        while i < j:
            k = ((j - i)/2) % 2
            mid = i + (j-i) // 2
            atemp, temp, tempa = nums[mid-1], nums[mid], nums[mid+1]
            if temp != atemp and temp != tempa:
                return temp
            elif temp == tempa:
                if k == 0:
                    i = mid + 2
                elif k == 1:
                    j = mid - 1
            elif temp == atemp:
                if k == 0:
                    j = mid - 2
                elif k == 1:
                    i = mid + 1
        return nums[i]


nums = [1,1,2,3,3,4,4,8,8]
# nums = [3,3,7,7,10,11,11]
# nums = [3]
# nums = [1,2,2]
# nums = [1,1,2]
mat = Solution()
mat.singleNonDuplicate(nums)
