#==================================================
#==>      Title: 4. 寻找两个正序数组的中位数
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/13/2021
#==================================================

"""
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
"""

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i = j = 0
        nums = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        nums += nums1[i:]
        nums += nums2[j:]
        i, j = 0, len(nums)-1
        mid = j // 2
        if j & 1:
            return (nums[mid] + nums[mid+1]) / 2
        else:
            return nums[mid]

mat = Solution()
nums1 = [1, 2, 9]
nums2 = [3, 4, 5, 6]
mat.findMedianSortedArrays(nums1, nums2)
