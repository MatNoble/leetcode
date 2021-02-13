#==================================================
#==>      Title: 215. 数组中的第K个最大元素
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 2/13/2021
#==================================================

"""
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
"""

from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k = len(nums) - k
        def partition(array, left, right):
            # 随机选取 pivot, 并交换至 right
            idx = random.randint(left, right)
            array[idx], array[right] = array[right], array[idx]
            pivot = array[right]
            i, j= left, right - 1
            while True:
                while i < right and array[i] <= pivot: i += 1
                while j >= left and array[j] >  pivot: j -= 1
                if i > j: break
                array[i], array[j] = array[j], array[i]
            array[right], array[i] = array[i], array[right]
            return i
        def quickQort(array, left, right):
            if left >= right: return
            ## 前序遍历
            index = partition(array, left, right)
            if self.k == index:
                return
            elif self.k < index:
                quickQort(array, left, index-1)
            else:
                quickQort(array, index+1, right)
        quickQort(nums, 0, len(nums)-1)
        return nums[self.k]

mat = Solution()
nums = [3,2,1,5,6,4]
k = 3
mat.findKthLargest(nums, k)
