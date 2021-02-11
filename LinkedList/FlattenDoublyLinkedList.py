# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/

# Definition for a Node.
# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child
from collections import deque

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        tmp = head
        stack = deque()
        while head:
            if head.child:
                if head.next: stack.appendleft(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            elif head.next is None and len(stack) > 0:
                head.next = stack.popleft()
                head.next.prev = head
            head = head.next
        return tmp
