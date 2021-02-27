# QUEUE - First-in-First-Out (FIFO)

In a FIFO data structure, the first element added to the queue will be processed first:

1. *Enqueue*: A new element is added at the end of the Queue
2. *Dequeue*: The first element in the queue is removed.

Efficient way to use Queue is to use a circular queue. We can use a fixed-size array and two pointers for tail and head. The goal is to reuse the wasted storage.

## Queue and BFS

One common application Breadth-First Search (BFS) is to find the shortest path from the root node to the target node.