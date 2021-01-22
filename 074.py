#==================================================
#==>      Title: search-a-2d-matrix
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/10/2021
#==================================================

"""
https://leetcode-cn.com/problems/search-a-2d-matrix/
"""

class Solution:
    def searchMatrix(self, matrix, target):
        n, m = len(matrix), len(matrix[0])
        if n == 0: return False
        nums = []
        for i in range(n): nums.append(matrix[i][0])
        nums.append(matrix[-1][-1])
        # first loop
        i, j = 0, len(nums) - 1
        while i < j-1:
            mid = i + (j-i) // 2
            if nums[mid] > target:
                j = mid
            elif nums[mid] < target:
                i = mid
            else:
                return True
        l = matrix[i][:]
        # second loop
        i, j = 0, m - 1
        while i <= j:
            mid = i + (j-i) // 2
            if l[mid] == target:
                return True
            elif l[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False

    def searchMatrix_(self, matrix, target):
        n, m = len(matrix), len(matrix[0])
        if n == 0: return False

        i, j = n-1, 0
        while i >=0 and j < m:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True
        return False
        

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 34

# matrix = [[1]]
# target = 1

mat = Solution()
mat.searchMatrix(matrix, target)
# mat.searchMatrix_(matrix, target)
