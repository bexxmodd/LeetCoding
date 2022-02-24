# Binary Tree

Each node of the tree will have a root value and a list of references to other nodes which are called child nodes. From graph view, a tree can also be defined as a directed acyclic graph which has $N$ nodes and $N-1$ edges.

Binary tree can have at most two children (left and right).

## Breadth-First Traversal (level-Order)

Level-order traversal is to traverse the tree level by level.

Breadth-First Search is an algorithm to traverse or search in data structures like a tree or a graph.

- The algorithm starts with a root node and visit the node itself first.
- Then traverse its neighbors, traverse its second level neighbors, traverse its third level neighbors, so on and so forth.

When we do breadth-first search in a tree, the order of the nodes we visited is in level order. Typically, we use a `queue` to help us to do BFS.

we can solve a tree problem recursively using a top-down approach or using a bottom-up approach

## Top-Down Recursion

"Top-down" means that in each recursive call, we will visit the node first to come up with some values, and pass these values to its children when calling the function recursively. So the **top-down** solution can be considered as a kind of preorder traversal.

```
def top_down(root, params):
    1. return specific value for null node
    2. update the answer if needed  // answer <-- params
    3. left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
    4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params
    5. return the answer if needed                      // answer <-- left_ans, right_ans
```

When you meet a tree problem, ask yourself two questions: Can you determine some parameters to help the node know its answer? Can you use these parameters and the value of the node itself to determine what should be the parameters passed to its children? If the answers are both yes, try to solve this problem using a "top-down" recursive solution.


### Check if Tree is Symmetric

A tree is symmetric if the left subtree is a mirror reflection of the right subtree. Two trees are a mirror of each other if:

1. Their two roots have the same values
2. The right subtree of each tree is a mirror reflection of the left subtree of the other tree.

```
def is_mirror(node1, node2):
    if not node1 and not node2
        return true;
    if not node1 or not node2
        return false;
    return node1.value == node2.value
        and is_mirror(node1.right, node2.left)
        and is_mirror(node1.left, node2.right)
```

This has time complexity of `O(n)` because we traverse the entire tree once.