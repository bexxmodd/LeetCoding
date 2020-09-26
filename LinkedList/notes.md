Each node in a singly-linked list contains not only the value but also a reference field to link to the next node.
By this way, the singly-linked list organizes all the nodes in a sequence.

Here is an example of a singly-linked list:
![example](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/12/screen-shot-2018-04-12-at-152754.png)

```
class SinglyListNode {
    int val;
    SinglyListNode next;
    SinglyListNode(int x) { val = x; }
}
```

If we want to add a new value after a given node `prev` we should:
1. Initialize a new node `cur` with the given value;
![first](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/26/screen-shot-2018-04-25-at-163224.png)

2. Link the "next" field of `cur` to `prev`'s next node next
![second](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/26/screen-shot-2018-04-25-at-163234.png)

3. Link the "next" field in `prev` to `cur`
![third](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/26/screen-shot-2018-04-25-at-163243.png)

example:
Let's insert a new value 9 after the second node 6.

We will first initialize a new node with value 9.
Then link node 9 to node 15.
Finally, link node 6 to node 9.

After insertion, our linked list will look like this:
![exampleNodes](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/12/screen-shot-2018-04-12-at-154238.png)

As we know, we use the head node head to represent the whole list.

So it is essential to update head when adding a new node at the beginning of the list.

1. Initialize a new node `cur`;
2. Link the new node to our original head node `head`.
3. Assign `cur` to `head`.


