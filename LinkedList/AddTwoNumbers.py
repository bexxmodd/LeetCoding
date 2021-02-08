# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = ListNode()
        curr = tmp
        first = l1
        second = l2
        carry = 0
        while first or second:
            x = 0
            y = 0
            if first:
                x = first.val
            if second:
                y = second.val
            total = x + y + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if first:
                first = first.next
            if second:
                second = second.next
        if carry > 0:
            curr.next = ListNode(carry)
        return tmp.next