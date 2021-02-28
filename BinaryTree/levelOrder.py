# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        values = []
        if not root:
            return values

        queue = deque([root])
        while queue:
            current_level = []
            for i in range(len(queue)):
                node = queue.popleft() # top node in queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current_level.append(node.val)
            values.append(current_level)
        return values