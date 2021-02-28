# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False
        return self.is_symmetric(root.left, root.right)
        
    def is_symmetric(self, a: TreeNode, b: TreeNode) -> bool:
        if not a and not b:
            return True
        if not a or not b:
            return False
        return (a.val == b.val) \
            and self.is_symmetric(a.left, b.right) \
            and self.is_symmetric(a.right, b.left)


