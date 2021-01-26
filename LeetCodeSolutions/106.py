#==================================================
#==>      Title: construct-binary-tree-from-inorder-and-postorder-traversal
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/21/2021
#==================================================
"""
https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder: return None
        root_val = postorder[-1]
        root_idx = inorder.index(root_val)

        root = TreeNode(root_val)
        root.left  = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx+1:], postorder[root_idx:-1])
        return root

    def traverse(self, root):
        if not root: return None
        print(root.val)
        self.traverse(root.left)
        self.traverse(root.right)


mat = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

root = mat.buildTree(inorder, postorder)
# 3, 9, 20, 15, 7
mat.traverse(root)
