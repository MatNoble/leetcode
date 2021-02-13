#==================================================
#==>      Title:                                     
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 
#==================================================

import random
from typing import List
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        self.k = k
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
            print(index, array)
            if self.k == index:
                return
            elif self.k < index:
                quickQort(array, left, index-1)
            else:
                quickQort(array, index+1, right)
        quickQort(arr, 0, len(arr)-1)
        return arr[:k]

mat = Solution()
arr = [1,3,5,7,2,4,6,8]
k = 2
mat.smallestK(arr, k)
