# Two-Pointer in Linked List

To detect a cycle we need to do use pointers one going faster than other and if they catch up we have a cycle:

1. If there is no cycle, the fast pointer will stop at the end of the linked list.

2. If there is a cycle, the fast pointer will eventually meet with the slow pointer.

What is a proper speed of two pointers?:

    - Slow pointer -> one step at a time
    - Fast pointer -> two step at a time
    - If the length of the cycle is $M$, after $M$ iterations the fast pointer will move one more cycle and catch up with slow pointer.

- If you want to return the node at which cycle starts have to use Floyd's Algorithm:
    - Move one pointer back to head and traverse until they meet.

- If you want to find the node at which two linked lists meet:
    - Use dict to store Nodes of the first linked list
    - traverse through the second linked list and if the value is in dict return the node

## Tips

1. Always examine if the node is null before you call the `next`
2. Carefully define the end conditions of your loop to avoid endless loop and null-point error.

------

# Classic Problems

## Reverse Linked List

Iterate the nodes in original order and change the direction of next towards the previous node. For example if we have `23 -> 6 -> 15 -> null`:
 We move the next node of the `6` as `23` then we move next node of `15` as `6` and next node of `23` as `null` this way we get `null <- 23 <- 6 <- 15`.

## Sort by putting odd nodes first then put even nodes next

- This can be done first putting the odd nodes in a linked list and the even nodes in another.
- Then link the evenList to the of the oddList
    - We need to track head and tail of each linked list

-----

# Doubly Linked List

Doubly linked list in addition to the `next` has one more reference field known as `prev`. This field allows to reference previous node.

Just like in a singly linked list:

1. We can't acces a random position in O(1).
2. We have to traverse from the head to get ith node we want.
3. Worst case time complexity will be O(n).

### Adding a node

The process of inserting a node `current` can be divided into two steps:

1. Link `current` with `prev`, where `next` is the original next node of `prev`.
2. Re-link the `prev` and `next` with `current`.

