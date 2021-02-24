# https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.head = None
        self.tail = None
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == len(self.queue):
            return False
        


    def deQueue(self) -> bool:
        pass

    def Front(self) -> int:
        if self.head:
            return self.head
        else:
            return -1

    def Rear(self) -> int:
        if self.tail:
            return self.tail
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.head

    def isFull(self) -> bool:
        return self.size == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
myCircularQueue = MyCircularQueue(3)
myCircularQueue.enQueue(1) # return True
myCircularQueue.enQueue(2) # return True
myCircularQueue.enQueue(3) # return True
myCircularQueue.enQueue(4) # return False
myCircularQueue.Rear()     # return 3
myCircularQueue.isFull()   # return True
myCircularQueue.deQueue()  # return True
myCircularQueue.enQueue(4) # return True
myCircularQueue.Rear()    # return 4