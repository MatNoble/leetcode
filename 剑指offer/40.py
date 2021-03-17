#==================================================
#==>      Title:                                     
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 
#==================================================

from typing import List
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # # 排序
        # return [] if not (arr and k) else sorted(arr)[:k]

        # # Counter
        # from collections import Counter
        # nums = Counter(arr)
        # num, res = 0, []
        # while True:
        #     while nums[num] and len(res) < k:
        #         res.append(num)
        #         nums[num] -= 1
        #     if len(res) == k:
        #         break
        #     num += 1
        # return res

        # 快排
        def exchange(a, i, j):
            a[i], a[j] = a[j], a[i]
            
        def poisition(arr, left, right):
            from random import randint
            x = randint(left, right)
            exchange(arr, x, right)
            pivot = arr[right]
            i, j = left, right-1
            while True:
                while i < right and arr[i] <= pivot: i += 1
                while j >= left and arr[j] >  pivot: j -= 1
                if i > j: break
                exchange(arr, i, j)
            exchange(arr, i, right)
            return i

        def quicksort(arr, i, j):
            if i >= j: return # base
            poi = poisition(arr, i, j)
            if self.k == poi:
                return
            elif self.k < poi:
                quicksort(arr, i, poi-1)
            else:
                quicksort(arr, poi+1, j)
        self.k = k-1
        quicksort(arr, 0, len(arr)-1)
        return arr[:k]

mat = Solution()
arr = [1, 2, 2, 3]
# arr = [1, 3, 5, 7, 2, 4, 2, 9, 4]
k = 3
mat.getLeastNumbers(arr, k)
