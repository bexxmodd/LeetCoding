# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
This method uses Floyd's Algorithm to detect 
 the first node where the cycle starts.
'''

class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        """Detects if we have a cycle"""
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return self.find_cycle_start(head, fast)
        return None
    
    def find_cycle_start(self, head, intersect):
        """Finds the Node where a cycle starts"""
        while True:
            # check first, then move pointers
            if head == intersect:
                return head
            
            head = head.next
            intersect = intersect.next
        return None