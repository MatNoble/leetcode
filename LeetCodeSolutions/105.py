#==================================================
#==>      Title: construct-binary-tree-from-preorder-and-inorder-traversal
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/21/2021
#==================================================
"""
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder: return None
        root_val = preorder[0]
        root_idx = inorder.index(root_val)

        root = TreeNode(root_val)
        root.left  = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        return root

    def traverse(self, root):
        if not root: return None
        print(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

mat = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

root = mat.buildTree(preorder, inorder)
mat.traverse(root)

