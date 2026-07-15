"""Stack and queue practice problems ordered from easy to medium.

Complete these without looking at solutions.py. Focus on explaining why the
newest or oldest waiting item must be processed next.
"""


def is_valid_parentheses(text: str) -> bool:
    """Return True when every bracket is closed in the correct order.

    LeetCode 20 - Easy

    The string contains only parentheses, square brackets, and curly brackets.
    Every closing bracket must match the most recent unmatched opening bracket.
    """
    pass


class MinStack:
    """Support stack operations and return the minimum value in O(1).

    LeetCode 155 - Medium

    Implement push, pop, top, and get_min without scanning the entire stack.
    Calls to pop, top, and get_min are only made when the stack is not empty.
    """

    def __init__(self):
        pass

    def push(self, value: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def get_min(self) -> int:
        pass


class MyQueue:
    """Implement a first-in, first-out queue using only two stacks.

    LeetCode 232 - Easy

    Implement push, pop, peek, and empty. Calls to pop and peek are only made
    when the queue is not empty.
    """

    def __init__(self):
        pass

    def push(self, value: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def peek(self) -> int:
        pass

    def empty(self) -> bool:
        pass


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """Find each nums1 value's next greater value in nums2.

    LeetCode 496 - Easy

    All values are unique, and every nums1 value appears in nums2. Return -1
    when there is no greater value to the right.
    """
    pass


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Return how many days each temperature waits for a warmer day.

    LeetCode 739 - Medium

    Return 0 for a day that has no warmer future temperature. Try to process
    each index with a monotonic stack instead of checking every future day.
    """
    pass
