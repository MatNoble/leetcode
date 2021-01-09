#==================================================
#==>      Title: remove-duplicates-from-sorted-array
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/9/2021
#==================================================

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
