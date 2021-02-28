# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        values = []
        self.preorder_traversal(root, values)
        return values
            
        
    def preorder_traversal(self, p: TreeNode, values: List[int]):
        if p:
            values.append(p.val)
            
            self.preorder_traversal(p.left, values)
            self.preorder_traversal(p.right, values)

# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        self.inorder_traversal(root, values)
        return values
        
        
    def inorder_traversal(self, p: TreeNode, values: List[int]):
        if p:            
            self.inorder_traversal(p.left, values)
            values.append(p.val)
            self.inorder_traversal(p.right, values)
        

# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        self.postorder_traversal(root, values)
        return values
        
    def postorder_traversal(self, p: TreeNode, values: List[int]):
        if p:
            self.postorder_traversal(p.left, values)
            self.postorder_traversal(p.right, values)
            values.append(p.val)
        