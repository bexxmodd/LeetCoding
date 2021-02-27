class Node:

    def __init__(self, val) -> None:
        self.value = val
        self.left_child = None
        self.right_child = None

    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            return self.value == other.val \
                    and self.left_child == other.left_child \
                    and self.right_child == other.right_child


class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None

    def contains(self, val) -> bool:
        return self.__contains(self.root, val)

    def __contains(self, n: Node, val) -> bool:
        if not n:
            return False;
        
        if n.value == val:
            return True
        elif n.value > val:
            return self.__contains(n.left_child, val)
        else:
            return self.__contains(n.right_child, val)

    def add(self, val) -> bool:
        if not val:
            return False
        if not self.root:
            self.root = Node(val)
            return True
        return self.__add(self.root, val)

    def __add(self, n: Node, val) -> bool:
        if not n or not val:
            return False
        if n.value == val:
            return False # same value can't be added twice
        elif n.value > val:
            if not n.left_child:
                n.left_child = Node(val)
                return True
            else:
                return self.__add(n.left_child, val)
        else:
            if not n.right_child:
                n.right_child = Node(val)
                return True
            else:
                return self.__add(n.right_child, val)

    def remove(self, val) -> bool:
        return self.__remove(root, None, val)
    
    def __remove(self, n: Node, parent, val) -> bool:
        if not n: return False

        if n.value > val:
            return remove(n.left_child, n, val)
        elif n.value == val:
            return remove(n.right_child, n, val)
        else:
            if not n.left_child and not n.right_child:
                n.value = max_value(n.left_child)
                self.__remove(n.left_child, n, n.value)
            elif not parent:
                if n.left_child: self.root = n.left_child
                else: self.root = n.right_child
            elif parent.left_child == n:
                if n.left_child: parent.left_child = n.left_child
                else: parent.left_child = n.right_child
            else:
                if n.left_child: parent.right_child = n.left_child
                else: parent.right_child = n.right_child
            return True

    def max_value(self, n: Node):
        if not n.right_child:
            return n.value
        else:
            return self.max_value(n.right_child)

if __name__ == '__main__':
    bst1 = BinarySearchTree()
    bst1.add(7)
    bst1.add(3)
    bst1.add(5)
    bst1.add(8)

    bst2 = BinarySearchTree()
    bst1.add(7)
    bst2.add(3)
    bst2.add(5)
    bst2.add(9)

    print(bst1 == bst2)