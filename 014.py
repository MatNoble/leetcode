#==================================================
#==>      Title: Leetcode-014-longestCommonPrefix                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/6/2021
#==================================================

'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
所有输入只包含小写字母 a-z 。
======================================================
输入: ["flower","flow","flight"]
输出: "fl"
======================================================
链接：https://leetcode-cn.com/problems/longest-common-prefix/
'''

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        setS = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(setS):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res

    def longestCommonPrefix_mm(self, strs):
        if not strs: return ""
        minS = min(strs)
        maxS = max(strs)
        for i, x in enumerate(minS):
            if x != maxS[i]:
                return maxS[:i]
        return minS

a = ["flower","flow","flight","fly","fool"]
mat = Solution()
mat.longestCommonPrefix(a)
mat.longestCommonPrefix_mm(a)

# print(min(a))
# print(max(a))

