#==================================================
#==>      Title: peak-index-in-a-mountain-array
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/10/2021
#==================================================

"""
https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/
"""

class Solution:
    def peakIndexInMountainArray(self, arr):
        i, j = 0, len(arr) - 1
        while i < j:
            mid = i + (j-i+1) // 2
            if arr[mid] > arr[mid-1]:
                i = mid
            else:
                j = mid - 1
        return j

arr = [0, 2, 4, 7, 13, 5, 2, 0]
mat = Solution()
index = mat.peakIndexInMountainArray(arr)
print(arr[index])
if arr[index] == max(arr):
    print(True)
else:
    print(False)
