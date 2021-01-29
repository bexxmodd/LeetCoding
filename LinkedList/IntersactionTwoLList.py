# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode) -> ListNode:
        d = {}
        curA = headA
        curB = headB

        # Add first linked list nodes in dict
        while curA:
            if curA in d:
                continue
            else:
                d[curA] = curA.val
            curA = curA.next

        # Traverse through the second llist
        #  if nodes are equal that's your intersaction node
        while curB:
            if curB in d:
                return curB
            else:
                curB = curB.next

        return None
