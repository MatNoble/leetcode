#==================================================
#==>      Title: 剑指 Offer 11. 旋转数组的最小数字
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/31/2021
#==================================================

"""
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
"""

from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers)-1
        while left < right:
            mid = left + (right - left) // 2
            while left < mid and numbers[left] == numbers[mid]: left += 1
            if numbers[left] < numbers[right]: return numbers[left]
            if numbers[left] <= numbers[mid]:
                left = mid+1
            else:
                right = mid
        return numbers[left]

mat = Solution()
numbers = [2, 3, 0, 1, 2]
# numbers = [1]
# numbers = [2, 0, 2, 2]
# numbers = [1, 2, 3]
# numbers = [2, 2, 0, 2, 2, 2, 2, 2, 2]
print(mat.minArray(numbers))
