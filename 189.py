#==================================================
#==>      Title: rotate-array
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/13/2021
#==================================================

"""
https://leetcode-cn.com/problems/rotate-array/
"""

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        #============
        #  1
        #============
        # k %= len(nums)
        # # nums[:] = nums[-k:] + nums[:-k]

        #============
        #  2
        #============
        # n = len(nums)
        # k %= n
        # nums += list(range(k))
        # for i in range(1, n+1):
        #     i = n - i
        #     nums[i+k] = nums[i]
        #     if i < k: nums[i] = nums[n + i]
        # del nums[n:]

        #============
        #  3
        #============
        def reverse(n, i, j):
            while i < j:
                n[i], n[j] = n[j], n[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)

nums = list(range(1, 8))
k = 3 + len(nums)

nums = [-1,-100,3,99]
k = 5

mat = Solution()
mat.rotate(nums, k)
print(nums)
