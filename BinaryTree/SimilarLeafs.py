# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        values1, values2 = [], []
        self.dfs(root1, values1)
        self.dfs(root2, values2)
        return values1 == values2
        
    def dfs(self, p: TreeNode, values: list):
        stack = deque()
        stack.append(p)
        while stack:
            curr = stack.pop()
            if self.is_leaf(curr):
                values.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
    def is_leaf(self, p: TreeNode) -> bool:
        return not p.left and not p.right