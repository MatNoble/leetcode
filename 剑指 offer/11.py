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
        flag , left, right = 0, 0, len(numbers)-1
        while left < right-1 and numbers[left] >= numbers[right]:
            mid = left + (right - left + 1) // 2
            while left < mid and numbers[left] == numbers[mid]:
                flag = 1
                left += 1
            if flag == 1:
                flag = 0
                continue
            if numbers[left] < numbers[mid]:
                left = mid
            else:
                right = mid
        return numbers[left] if numbers[left]<numbers[right] else numbers[right]

mat = Solution()
numbers = [2, 3, 0, 1, 2]
# numbers = [1]
# numbers = [2, 0, 2, 2]
# numbers = [1, 2, 3]
# numbers = [2, 2, 0, 2, 2, 2, 2, 2, 2]
print(mat.minArray(numbers))
