# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = ListNode()
        head = tmp
        
        while l1 and l2:
            if l1.val > l2.val:
                tmp.next = l2
                l2 = l2.next
            else:
                tmp.next = l1
                l1 = l1.next
            tmp = tmp.next
            
        if l1:
            tmp.next = l1
        else:
            tmp.next = l2
            
        return head.next