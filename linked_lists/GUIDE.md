# Linked Lists: Follow the Arrows

Linked lists are chains of nodes. Each node stores:

1. A value
2. A pointer to the next node

```text
head
 ↓
[1 | next] → [2 | next] → [3 | None]
```

Unlike a Python list, you cannot jump directly to an index. You must start at
`head` and follow the arrows one node at a time.

## Real-World Analogy: A Train

Think of every node as a train car. Each car is coupled to exactly one next car.

- `head` is the engine at the front.
- `node.val` is what the car is carrying.
- `node.next` is the coupling to the next car.
- `None` means there is no car after this one.

Most linked-list problems are really asking you to carefully change or compare
these couplings without losing the rest of the train.

**Golden rule:** Save the next node before changing a pointer.

## The Node Template

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## When to Recognize This Pattern

Linked-list techniques usually apply when the prompt says:

- Reverse or reorder a linked list
- Detect a cycle or find where a cycle begins
- Find the middle of a linked list
- Merge sorted linked lists
- Remove a node relative to the end
- Solve the problem in `O(1)` extra space

The most important clue is that you need to move through nodes or rewire
`next` pointers without copying all values into another data structure.

## Pattern 1: Reverse Pointers

Use three references:

- `previous` remembers the part already reversed.
- `current` is the node being changed.
- `next_node` saves the untouched remainder of the list.

```python
previous = None
current = head

while current:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

return previous
```

Memorize the movement:

```text
save next → reverse arrow → move previous → move current
```

## Pattern 2: Slow and Fast Pointers

Use two runners that move at different speeds:

```python
slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

This works because:

- If there is no cycle, `fast` reaches the end.
- If there is a cycle, `fast` eventually catches `slow`.
- When `fast` moves twice as quickly, `slow` reaches the middle when `fast`
  reaches the end.

## Pattern 3: Two Pointers With a Gap

To find a node relative to the end, move `fast` ahead first. Then move both
pointers together while keeping the gap fixed.

```python
dummy = ListNode(0, head)
slow = fast = dummy

for _ in range(n + 1):
    fast = fast.next

while fast:
    slow = slow.next
    fast = fast.next

slow.next = slow.next.next
return dummy.next
```

The dummy node removes special-case logic when the head itself must be removed.

## Pattern 4: Build With a Dummy Node

When creating or merging a list, use a dummy node so every append works the
same way:

```python
dummy = ListNode()
tail = dummy

while condition:
    tail.next = chosen_node
    tail = tail.next

return dummy.next
```

`dummy` is a temporary starting point. The real answer begins at `dummy.next`.

## Interview Checklist

Before coding, ask:

1. Can the list be empty?
2. Can the head node change?
3. Is there guaranteed to be a valid `n`?
4. Am I comparing node identity or node values?
5. Do I need a dummy node to avoid a head special case?

Before finishing, test:

- Empty list
- One node
- Two nodes
- Removing or changing the head
- Even and odd list lengths
- A cycle that points back to the head

## Complexity Cheat Sheet

- One full traversal: `O(n)` time
- Two pointers still traversing once: `O(n)` time
- Rewiring pointers in place: `O(1)` extra space
- Merging lists of lengths `n` and `m`: `O(n + m)` time

The goal is not to memorize every linked-list problem. Memorize these pointer
movements, then learn to recognize which one the problem is asking for.
