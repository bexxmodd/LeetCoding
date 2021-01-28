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
        self.size = 0
        
    def __str__(self):
        string = ""
        tmp = self.val
        while tmp:
            string += f'{tmp.val} -> '
            tmp = tmp.next
        return string

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if index < 0:
            return -1
        
        tmp = self.val
        pointer = 0
        while tmp is not None:
            if pointer == index:
                return tmp.val
            tmp = tmp.next
            pointer += 1
        return -1


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.val
        self.val = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if self.val is None:
            self.val = new_node

        tmp = self.val
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be 
         appended to the end of linked list. If index is greater 
         than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
            self.size += 1
        else:
            new_node = Node(val)
            current = self.val
            for i in range(1, index):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size or self.val is None:
            return
        elif index == 0:
            self.val = self.val.next
            self.size -= 1
        else:
            current = self.val
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)
print(myLinkedList.get(1))
print(myLinkedList)  
myLinkedList.deleteAtIndex(0)
print(myLinkedList)
print(myLinkedList.get(0))    
