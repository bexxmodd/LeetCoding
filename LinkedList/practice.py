class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        
    def __str__(self) -> str:
        linkedlist = ''
        tmp = self.val
        while tmp:
            linkedlist += str(tmp.val) + " -> "
            tmp = tmp.next
        return linkedlist + 'null'

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
            If the index is invalid, return -1.
        """
        pass

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
            After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.val
        self.val = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if self.val is None:
            self.val = new_node
            return
        
        last = self.val
        while last.next:
            last = last.next
        last.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
            If index equals to the length of linked list, the node will be
            appended to the end of linked list. If index is greater than the length, 
            the node will not be inserted.
        """
        pass
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        pass

if __name__ == '__main__':
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
    obj.addAtHead(10)
    obj.addAtHead(112)
    param_1 = obj.get(2)
    print(param_1)
    obj.addAtHead(1)
    obj.addAtTail(2)
    obj.addAtIndex(1, 3)
    print(obj)
    obj.deleteAtIndex(1)