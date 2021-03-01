# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    # DFS with stack
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        stack = deque()
        stack.appendleft((root, root.val))
        while stack:
            curr, value = stack.popleft()
            if self.is_leaf(curr) and value == targetSum:
                return True
            if curr.left:
                stack.appendleft((curr.left, value+curr.left.val))
            if curr.right:
                stack.appendleft((curr.right, value+curr.right.val))
        return False

    def is_leaf(self, p: TreeNode) -> bool:
        return not p.left and not p.right

