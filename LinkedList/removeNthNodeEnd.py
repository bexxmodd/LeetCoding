# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(
        self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
            
        size = self.get_size(head)
        if n > size or n < -1 or size == 1:
            return None

        # As we have size the nth node from the back will be
        # (size - n + 1)th node from the start 
        # remove 1 as the index starts from 0
        index = size - n
        curr = head

        # Remove if the nth node ends up being head
        if index == 0:
            curr = curr.next
            return curr

        # Iterate until we reach nth node
        for i in range(index - 1):
            curr = curr.next

        # Remove nth node
        curr.next = curr.next.next              
        return head

    def get_size(self, head: ListNode) -> int:
        if head is None:
            return None
        size = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            size += 1
        return size