#==================================================
#==>      Title: count-complete-tree-nodes                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/21/2021
#==================================================

"""
https://leetcode-cn.com/problems/count-complete-tree-nodes/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        left, right = root, root
        hl, hr = 0, 0
        while left != None:
            left = left.left
            hl += 1
        while right != None:
            right = right.right
            hr += 1
        if hl == hr: return pow(2, hl) - 1
        return 1 + self.countNodes(root.left) + self.countNodes
