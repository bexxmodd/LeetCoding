# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Sanity check
        if head is None or head.next is None:
            return head
            
        # First node will be start of a linked list with odd nodes
        # Second node will start a linked list with even nodes
        odds, evens = head, head.next

        # Keep track of head of the evens as it will be attached
        #  to the linked list with odd nodes
        evens_head = evens

        while evens and evens.next:
            odds.next = evens.next
            odds = odds.next
            evens.next = odds.next
            evens = evens.next
        
        # Attach the head of evens to the tail of odds
        odds.next = evens_head
        return head