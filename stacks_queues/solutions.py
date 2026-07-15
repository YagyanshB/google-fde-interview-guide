"""Annotated solutions for the stack and queue practice problems."""


def is_valid_parentheses(text: str) -> bool:
    """Match every closing bracket with the latest opening bracket."""
    matching_open = {")": "(", "]": "[", "}": "{"}
    stack = []

    for character in text:
        if character in matching_open:
            # A closer is invalid if nothing is waiting or the newest opener
            # has a different bracket type.
            if not stack or stack.pop() != matching_open[character]:
                return False
        else:
            stack.append(character)  # Save this opener until it is closed.

    return not stack  # Any leftover opener was never closed.


# Time: O(n) because every character is pushed or checked once.
# Space: O(n) because every character could be an opening bracket.


class MinStack:
    """Store each value together with the minimum at that point."""

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if self.stack:
            current_minimum = min(value, self.stack[-1][1])
        else:
            current_minimum = value

        # Saving the current minimum makes get_min a direct lookup.
        self.stack.append((value, current_minimum))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        return self.stack[-1][1]


# Time: O(1) for push, pop, top, and get_min.
# Space: O(n) because every pushed value stores one value-minimum pair.


class MyQueue:
    """Reverse values between two stacks to preserve first-in-first-out order."""

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, value: int) -> None:
        self.input_stack.append(value)  # New values wait in arrival order.

    def _move_input_if_needed(self) -> None:
        if not self.output_stack:
            while self.input_stack:
                # Reversing the input puts the oldest value on top.
                self.output_stack.append(self.input_stack.pop())

    def pop(self) -> int:
        self._move_input_if_needed()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._move_input_if_needed()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack


# Time: O(1) amortized for push, pop, peek, and empty. One pop can trigger an
# O(n) transfer, but each value transfers from input to output only once.
# Space: O(n) because the two stacks together store every queued value.


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """Map each value to the next greater value found by a decreasing stack."""
    next_greater = {}
    stack = []

    for value in nums2:
        # This value is the first greater value to the right for every smaller
        # value currently waiting at the top of the stack.
        while stack and value > stack[-1]:
            smaller_value = stack.pop()
            next_greater[smaller_value] = value

        stack.append(value)

    # Values left in the stack never found a greater value to their right.
    return [next_greater.get(value, -1) for value in nums1]


# Time: O(n + m) because each nums2 value is pushed and popped at most once,
# then each of the m nums1 values is looked up once.
# Space: O(n) for the stack and next-greater lookup table.


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Resolve cooler days with a decreasing stack of waiting indices."""
    answer = [0] * len(temperatures)
    stack = []

    for current_day, current_temperature in enumerate(temperatures):
        while stack and current_temperature > temperatures[stack[-1]]:
            cooler_day = stack.pop()
            answer[cooler_day] = current_day - cooler_day

        # Store the index because the answer needs the distance between days.
        stack.append(current_day)

    return answer


# Time: O(n) because every index is pushed once and popped at most once.
# Space: O(n) because the stack may hold every index when temperatures fall.
