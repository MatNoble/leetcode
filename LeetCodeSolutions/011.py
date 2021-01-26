#==================================================
#==>      Title: container-with-most-water
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/9/2021
#==================================================

class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        max_ = area = (j-i)*min(height[i], height[j])
        while i < j:
            if height[i] <= height[j]:
                i += 1
                if height[i] <= height[i-1]:
                    continue
            else:
                j -= 1
                if height[j] <= height[j+1]:
                    continue
            area = (j-i)*min(height[i], height[j])
            max_ = max(max_, area)
        return max_

list_ = [1,8,6,2,5,4,8,3,7]
mat = Solution()
mat.maxArea(list_)
