# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Node) -> 'Node':
        cur = head
        tmp = None
        while cur:
            if cur.child:
                cur.next = cur.child
                cur.prev = cur
            cur = cur.next
        return head