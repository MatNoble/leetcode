#==================================================
#==>      Title: minimum-window-substring                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/18/2021
#==================================================

"""
https://leetcode-cn.com/problems/minimum-window-substring/
"""

class Solution:
    def minWindow(self, s, t):
        ks, kt = len(s), len(t)
        window, need = dict(zip(s, [0]*ks)), dict(zip(t, [0]*kt))
        for i in range(len(t)): need[t[i]] += 1
        
        left, right, valid, length = 0, 0, 0, ks+1
        while right < ks:
            # 移动右边界
            temp = s[right]
            # 判断
            if temp in need:
                window[temp] += 1
                if window[temp] <= need[temp]: valid += 1
            right += 1 # 右边界右移
            while valid == kt:
                # 判断 + 记录
                if right - left < length: start, length = left, right - left
                temp = s[left]
                if temp in need:
                    if window[temp] == need[temp]: valid -= 1
                    window[temp] -= 1
                left += 1
        return  "" if length == ks+1 else s[start : start+length]

mat = Solution()
# s = "ADOBECODEBANC"
# s = "EBBANCF"
# t = "ABC"
s = 'aa'
t = 'aa'
mat.minWindow(s, t)
