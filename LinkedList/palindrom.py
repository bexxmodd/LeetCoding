# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        current = head
        while current:
            # Append values of the linked list to regular list
            values.append(current.val)
            current = current.next
        # Check if current list and reversed list are equal
        return values == values[::-1]
