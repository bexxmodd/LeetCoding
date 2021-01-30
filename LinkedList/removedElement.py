# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Create a dummy Nodw who's next node is current head
        dummy = ListNode(next=head)
        prev = dummy
        current = dummy.next
        while current:
            # if current equals value remove node 
            #  by linking its next to previous' next
            if current.val == val:
                prev.next = current.next
                
            # if value is not equal current node move
            #  both curr and prev to the next
            else:
                prev = prev.next
            current = current.next
        return dummy.next