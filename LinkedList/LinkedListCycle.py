# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        fast_node = head
        current = head
        while current:
            if fast_node.next is None or fast_node.next.next is None:
                return False
            current = current.next
            fast_node = fast_node.next.next
            if current == fast_node:
                return True