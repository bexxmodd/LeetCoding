# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self, l1: ListNode, l2: ListNode) -> ListNode:
        first = l1
        second = l2
        merged = ListNode()
        while first.next or second.next:
            if first is None:
                merged.next = second
                second = second.next
            elif second is None:
                merged.next = first
                first = first.next
            elif first.val <= second.val:
                merged.next = first
                first = first.next
            elif first.val > second.val:
                merged.next = second
                second = second.next
        return merged