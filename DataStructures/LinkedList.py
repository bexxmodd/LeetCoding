class Node:

    def __init__(self, data: int):
        self.data = data
        self.next = None;

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data: int) -> None:
        # If List is empty we setup data as the head
        if self.head == None:
            self.head = Node(data)
            return
        # If List is not empty, add data and update next
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(data)

    def prepand(self, data: int) -> None:
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def delete_with_value(self, data: int) -> None:
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def count_nodes(self) -> int:
        count = 0
        current = self.head
        while self.next != None:
            current = current.next
            count += 1
        return count


