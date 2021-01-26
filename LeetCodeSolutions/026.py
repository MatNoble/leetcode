#==================================================
#==>      Title: remove-duplicates-from-sorted-array
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/9/2021
#==================================================

"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    def removeDuplicates(self, nums):
        i, j = 0, 0
        while j < len(nums):
            if i == 0 or nums[i-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

mat = Solution()
list_ = [1, 1, 2]
index = mat.removeDuplicates(list_)
print(list_[:index])
