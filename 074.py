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
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        l = []
        i = 0
        while i < len(matrix):
            l.append(matrix[i][0])
            i += 1
        l.append(matrix[-1][-1])
        print(l)
        # first loop
        i, j = 0, len(l) - 1
        while i < j-1:
            mid = i + (j-i) // 2
            if l[mid] == target:
                return True
            elif l[mid] > target:
                j = mid
            else:
                i = mid
        l = matrix[i][:]
        # second loop
        i, j = 0, len(l) - 1
        while i <= j:
            mid = i + (j-i) // 2
            if l[mid] == target:
                return True
            elif l[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

# matrix = [[1]]
# target = 1

mat = Solution()
mat.searchMatrix(matrix, target)
