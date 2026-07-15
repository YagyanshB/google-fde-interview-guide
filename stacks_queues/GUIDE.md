# Stacks and Queues: Control the Order

Stacks and queues both store items in an order. The difference is which item
you are allowed to remove next.

```text
Stack: last in, first out (LIFO)
Queue: first in, first out (FIFO)
```

In Python, a list works well as a stack. For a queue, use `collections.deque`
so removing from the front stays efficient.

## Real-World Analogy: Plates and a Waiting Line

Think of a stack as a pile of cafeteria plates:

- You place a clean plate on top.
- You take the top plate first.
- The most recently added plate leaves first.

Think of a queue as a line at the cafeteria register:

- New people join at the back.
- The person at the front is served first.
- The person who arrived first leaves first.

The key interview question is: **Which waiting item should be processed next?**

## The Python Templates

### Stack

```python
stack = []

stack.append(value)  # Push onto the top.
top = stack[-1]  # Look at the top without removing it.
value = stack.pop()  # Remove and return the top.
```

### Queue

```python
from collections import deque

queue = deque()

queue.append(value)  # Add to the back.
front = queue[0]  # Look at the front without removing it.
value = queue.popleft()  # Remove and return the front.
```

Avoid `list.pop(0)` for a queue. Every remaining item must shift left, so one
removal costs `O(n)` instead of `O(1)`.

## When to Recognize These Patterns

Stack techniques usually apply when the prompt says:

- Match opening and closing symbols
- Undo or reverse recent actions
- Evaluate expressions
- Process nested structures
- Find the next greater or smaller value
- Track a running minimum or maximum

Queue techniques usually apply when the prompt says:

- Process items in arrival order
- Build a first-in, first-out data structure
- Explore a graph or tree level by level
- Schedule tasks fairly
- Buffer work before it is processed

The strongest stack clue is that the most recent unfinished item matters. The
strongest queue clue is that the oldest waiting item matters.

## Pattern 1: Matching Pairs

Push opening symbols. When a closing symbol appears, it must match the opening
symbol on top of the stack.

```python
pairs = {")": "(", "]": "[", "}": "{"}
stack = []

for character in text:
    if character in pairs:
        if not stack or stack.pop() != pairs[character]:
            return False
    else:
        stack.append(character)

return not stack
```

Why only check the top? Nested pairs must close in reverse order. The most
recent opening symbol is the first one that must be closed.

## Pattern 2: Store Extra Information

Sometimes a stack must answer more than `push` and `pop`. Store the extra fact
you will need later together with every value.

For a minimum stack, each entry can remember the minimum so far:

```python
stack.append((value, minimum_so_far))
```

Then the current minimum is always available at the top in `O(1)` time. You do
not need to scan the whole stack after a value is removed.

## Pattern 3: Queue Using Two Stacks

One stack receives new items. A second stack serves the oldest items.

```text
input stack:  [1, 2, 3]
transfer all items
output stack: [3, 2, 1]  ← pop 1 first
```

```python
if not output_stack:
    while input_stack:
        output_stack.append(input_stack.pop())

return output_stack.pop()
```

Only transfer when the output stack is empty. Each item moves from input to
output at most once, so a sequence of operations averages `O(1)` per call.

## Pattern 4: Monotonic Stack

A monotonic stack keeps its values in increasing or decreasing order. It is
useful when each item needs to find the next greater or smaller item.

For a decreasing stack of indices:

```python
stack = []

for index, value in enumerate(values):
    while stack and value > values[stack[-1]]:
        previous_index = stack.pop()
        answer[previous_index] = index - previous_index

    stack.append(index)
```

The current value resolves every smaller value waiting on the stack. Store
indices when the answer depends on distance or position. Store values when the
answer only needs the matching value.

Each index is pushed once and popped at most once. Even with a nested `while`
loop, the total work is `O(n)`, not `O(n²)`.

## Interview Checklist

Before coding, ask:

1. Which item must come out next: newest or oldest?
2. Do I need values, indices, or both?
3. What must be remembered when an item is pushed?
4. What condition causes waiting items to be popped?
5. What should happen when the structure is empty?

Before finishing, test:

- Empty input
- One item
- Already increasing or decreasing input
- Duplicate values
- A closing symbol with no opener
- Items that never find a greater or smaller value

## Complexity Cheat Sheet

- Stack `append` and `pop`: `O(1)`
- Deque `append` and `popleft`: `O(1)`
- Matching every character once: `O(n)` time and `O(n)` space
- Two-stack queue: `O(1)` amortized per operation
- Monotonic stack: `O(n)` time and `O(n)` space

The goal is not to memorize every stack or queue problem. First decide which
item must be processed next, then choose the structure that preserves that
order.
