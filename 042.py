#==================================================
#==>      Title: trapping-rain-water
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/20/2021
#==================================================

"""
https://leetcode-cn.com/problems/trapping-rain-water/
"""

class Solution:
    def trapBruteForce(self, height):
        if not height: return 0
        res, n = 0, len(height)
        for i in range(n):
            l_max, r_max = 0, 0
            j = i
            while j >= 0:
                l_max = max(height[j], l_max)
                j -= 1
            j = i
            while j < n:
                r_max = max(height[j], r_max)
                j += 1
            res += min(l_max, r_max) - height[i]
        return res

    def trap(self, height):
        if not height: return 0
        res, n = 0, len(height)
        l_max, r_max = [height[0]]*n, [height[-1]]*n
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i-1])
            j = n-i-1
            r_max[j] = max(height[j], r_max[j+1])
        for i in range(n):
            res += min(l_max[i], r_max[i]) - height[i]
        return res

    def trapOptimal(self, height):
        if not height: return 0
        res, n = 0, len(height)
        left, right = 0, n-1
        l_max, r_max = height[0], height[-1]
        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
mat = Solution()
print(mat.trapBruteForce(height))
print(mat.trap(height))
print(mat.trapOptimal(height))
