#==================================================
#==>      Title: find-smallest-letter-greater-than-target
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/10/2021
#==================================================

"""
https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/submissions/
"""

class Solution:
    def nextGreatestLetter(self, letters, target):
        if target >= letters[-1]:
            return letters[0]
        i, j = 0, len(letters) - 1
        while i < j:
            mid = i + (j-i) // 2
            if letters[mid] <= target:
                i = mid + 1
            else:
                j = mid
        return letters[j]

letters = ["c","f","j"]
targets = ["a", "c", "d", "g", "j", "k"]
solutions = ["c", "f", "f", "j", "c", "c"]
mat = Solution()
k = 0
while True:
    temp = mat.nextGreatestLetter(letters, targets[k])
    if temp != solutions[k]:
        print(f'在第 {k+1} 位出错')
        break
    k += 1
    if k == len(targets):
        print('Bingo')
        break
