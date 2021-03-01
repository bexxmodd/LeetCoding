# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left),
                        self.maxDepth(root.right))