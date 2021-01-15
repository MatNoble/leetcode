#==================================================
#==>      Title: next-greater-element-i
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/15/2021
#==================================================

"""
https://leetcode-cn.com/problems/next-greater-element-i/
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums1)
        res = [-1] * n
        nums = {}
        for idx, val in enumerate(nums2): nums[val] = idx
        for i in range(n):
            j = nums[nums1[i]] + 1
            while j < len(nums2):
                if nums1[i] < nums2[j]:
                    res[i] = nums2[j]
                    break
                j += 1
        return res



nums1 = [4,1,2]
nums2 = [1,3,4,2]

nums1 = [2,4]
nums2 = [1,2,3,4]

mat = Solution()
mat.nextGreaterElement(nums1, nums2)
