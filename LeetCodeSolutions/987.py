#==================================================
#==>      Title:                                     
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 
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
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:     
        vertical = collections.defaultdict(list)

        queue = collections.deque()
        queue.append((root, 0, 0))
        while queue:
            node, row, col = queue.popleft()
            vertical[col].append([row, node.val])
            if node.left:
                queue.append((node.left, row+1, col-1))
            if node.right:
                queue.append((node.right, row+1, col+1))
        # def dfs(node,row=0,col=0):
        #     if node is None: return None
        #     dfs(node.left  ,row+1,col-1)
        #     dfs(node.right ,row+1,col+1)
        #     vertical[col].append([row, node.val]) 
        # dfs(root)
        return [ [node_value for row_value, node_value in sorted(values)] for col_value, values in sorted(vertical.items())]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

mat = Solution()
mat.verticalTraversal(root)
