# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        current = head.next
        prev = head
        while current:
            nex = current.next
            current.next = prev
            prev = current
            current = nex
        head = prev
        return head