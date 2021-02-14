# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        tail = head
        
        # Calculate length but start with 1 as the loop'll
        # stop just before the last value in the linked list
        length = 1
        while tail.next:
            length += 1
            tail = tail.next
            
        # Check if the k exceeds the number of nodes no
        # no need to run extra cycle
        k %= length
        if k == 0: return head
        
        # New head will start from length - k
        start_pointer = length - k
        tail.next = head
        while start_pointer > 0:
            tail = tail.next
            start_pointer -= 1

        new_head = tail.next
        tail.next = None
        return new_head