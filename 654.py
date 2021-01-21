#==================================================
#==>      Title: maximum-binary-tree
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/21/2021
#==================================================
"""
https://leetcode-cn.com/problems/maximum-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums: return None
        val_max = max(nums)
        idx = nums.index(val_max)
        root = TreeNode(val_max)
        root.left  = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root

    def traverse(self, root):
        if not root: return None
        print(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

mat = Solution()
nums = [3,2,1,6,0,5]
root = mat.constructMaximumBinaryTree(nums)
# 6, 3, 2, 1, 5, 0
mat.traverse(root)
