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
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # ## 排序
        # nums.sort(reverse=True)
        # return nums[k-1]

        ## 二叉堆
        size = len(nums)
        flag = 0
        if k > size//2:
            nums = [-num for num in nums]
            k = size - k + 1
            flag = 1
        L = []
        for index in range(k):
            heapq.heappush(L, nums[index])

        for index in range(k, size):
            if nums[index] > L[0]:
                heapq.heapreplace(L, nums[index])
        return -L[0] if flag else L[0]

        # ## 计数排序
        # from collections import Counter
        # dict = Counter(nums)
        # # dict = {}
        # # for num in nums:
        # #     if num not in dict:
        # #         dict[num] = 1
        # #     else:
        # #         dict[num] += 1
        # i, num = 0, max(nums)
        # while True:
        #     if num in dict and dict[num]:
        #         dict[num] -= 1
        #         i += 1
        #         if i == k: break
        #     else:
        #         num -= 1
        # return num

        # “假”快排
        # self.k = len(nums) - k
        # def partition(array, left, right):
        #     # 随机选取 pivot, 并交换至 right
        #     idx = random.randint(left, right)
        #     array[idx], array[right] = array[right], array[idx]
        #     pivot = array[right]
        #     i, j= left, right - 1
        #     while True:
        #         while i < right and array[i] <= pivot: i += 1
        #         while j >= left and array[j] >  pivot: j -= 1
        #         if i > j: break
        #         array[i], array[j] = array[j], array[i]
        #     array[right], array[i] = array[i], array[right]
        #     return i
        # def quickSort(array, left, right):
        #     if left >= right: return
        #     ## 前序遍历
        #     index = partition(array, left, right)
        #     if self.k == index:
        #         return
        #     elif self.k < index:
        #         quickSort(array, left, index-1)
        #     else:
        #         quickSort(array, index+1, right)
        # quickSort(nums, 0, len(nums)-1)
        # return nums[self.k]

mat = Solution()
nums = [3,2,1,5,6,4]
k = 5
mat.findKthLargest(nums, k)
