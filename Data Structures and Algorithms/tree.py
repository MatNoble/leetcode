#==================================================
#==>      Title: Tree                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/29/2021
#==================================================

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []
        stack, res = [root], []
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right: stack.append(tmp.right)
            if  tmp.left: stack.append(tmp.left)
        return res

    def preorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        def preorder(root):
            if not root: return []
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
            return res
        res = []
        preorder(root)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        cur, stack, res = root, [], []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            res.append(tmp.val)
            cur = tmp.right
        return res

    def inorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        def inorder(root):
            if not root: return []
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            return res
        res = []
        inorder(root)
        return res
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []
        stack, res = [(0, root)], []
        while stack:
            flag, node = stack.pop()
            if flag == 1 or (not (node.left or node.right)):
                res.append(node.val)
            else:
                stack.append((1, node))
                if node.right: stack.append((0, node.right))
                if  node.left: stack.append((0, node.left))
        return res

    def postorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        def postorder(root):
            if not root: return []
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
            return res
        res = []
        postorder(root)
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, q = [], [root]
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                node = q.pop(0)
                level.append(node.val)
                if  node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res

    def maxDepth(self, root: TreeNode) -> int:
        def bottomUp(root):
            return 0 if not root else max(bottomUp(root.left), bottomUp(root.right)) + 1
        def topDown(root, depth):
            return depth if not root else max(topDown(root.left, depth+1), topDown(root.right, depth+1))
        return topDown(root, 0), bottomUp(root)

mat = Solution()
## 前序
root = TreeNode(1)

root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right = TreeNode(5)
root.right.left = TreeNode(6)
print("\n前序输出：")
print(mat.preorderTraversal(root))
print(mat.preorderTraversalRecursion(root))

## 中序
root = TreeNode(4)

root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right = TreeNode(6)
root.right.left = TreeNode(5)
print("\n中序输出：")
print(mat.inorderTraversal(root))
print(mat.inorderTraversalRecursion(root))

## 后序
root = TreeNode(6)

root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

root.right = TreeNode(5)
root.right.left = TreeNode(4)
print("\n后序输出：")
print(mat.postorderTraversal(root))
print(mat.postorderTraversalRecursion(root))

## 层序
root = TreeNode(1)

root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
print("\n层序输出：")
print(mat.levelOrder(root))

print('\n最大树深度:')
mat.maxDepth(root)
