#==================================================
#==>      Title: plus-one                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/25/2021
#==================================================

"""
https://leetcode-cn.com/problems/plus-one/
"""

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # n = len(digits)-1
        # while n >= 0:
        #     digits[n] += 1
        #     if digits[n] == 10:
        #         digits[n] = 0
        #         n -= 1
        #     else:
        #         break
        # if digits[0] == 0 and digits[-1] == 0:
        #     digits.insert(0, 1)
        # return digits
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i], carry = (carry + digits[i]) % 10, (carry + digits[i]) // 10
            if not carry: return digits
        return [carry] + digits

mat = Solution()
digits = [9, 9, 9]
# digits = [0]
# digits = [0, 0]
mat.plusOne(digits)
