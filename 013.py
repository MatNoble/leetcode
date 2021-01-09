#==================================================
#==>      Title: Leetcode-013-romanToInt                             
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/6/2021
#==================================================

'''
======================================================
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
======================================================

链接：https://leetcode-cn.com/problems/roman-to-integer/
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        res = 0
        for i in range(len(s)-1):
            temp = dic[s[i]]
            if dic[s[i]]<dic[s[i+1]]:
                res -= temp
            else:
                res += temp
        return res+dic[s[-1]]

x = 'IV'
x = 'LVIII'
x = 'MCMXCIV'
mat = Solution()
mat.romanToInt(x)
