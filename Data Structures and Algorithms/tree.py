#==================================================
#==>      Title: Tree                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/29/2021
#==================================================

from typing import List
import collections
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
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def preorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        def preorder(root):
            if not root: return
            res.append(root.val) ## 前序
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
            node = stack.pop()
            res.append(node.val)
            cur = node.right
        return res

    def inorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        def inorder(root):
            if not root: return
            inorder(root.left)
            res.append(root.val) ## 中序
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
                if node.right:
                    stack.append((0, node.right))
                if node.left:
                    stack.append((0, node.left))
        return res

    def postorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        def postorder(root):
            if not root: return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)  ## 后序
            return res
        res = []
        postorder(root)
        return res

    def levelTraversalLeft(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            n, level = len(queue), []
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

    def levelTraversalRight(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            n, level = len(queue), []
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            res.append(level)
        return res

    def levelTraversal(self, root: TreeNode, k=-1) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            n, level = len(queue), collections.deque()
            for _ in range(n):
                node = queue.popleft()
                if k == -1: ## 左 --> 右
                    level.append(node.val)
                else:       ## 右 --> 左
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(level))
        return res

    def levelTraversalJagged(self, root: TreeNode, k=-1) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            n, level = len(queue), collections.deque()
            k *= -1
            for _ in range(n):
                node = queue.popleft()
                if k == -1: ## 左 --> 右
                    level.append(node.val)
                else:       ## 右 --> 左
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(level))
        return res

    def maxDepth(self, root: TreeNode) -> int:
        def bottomUp(root):
            return 0 if not root else max(bottomUp(root.left), bottomUp(root.right)) + 1
        def topDown(root, depth=0):
            return depth if not root else max(topDown(root.left, depth+1), topDown(root.right, depth+1))
        return topDown(root), bottomUp(root)

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
# root = TreeNode(6)

# root.left = TreeNode(3)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)

# root.right = TreeNode(5)
# root.right.left = TreeNode(4)
# print("\n后序输出：")
# print(mat.postorderTraversal(root))
# print(mat.postorderTraversalRecursion(root))

# ## 层序
root = TreeNode(1)

root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
print("\n层序输出：")
print(mat.levelTraversalLeft(root))
print(mat.levelTraversalRight(root))

print(mat.levelTraversal(root))
print(mat.levelTraversal(root, 1))

print(mat.levelTraversalJagged(root))
print(mat.levelTraversalJagged(root, 1))

print('\n最大树深度:')
mat.maxDepth(root)
