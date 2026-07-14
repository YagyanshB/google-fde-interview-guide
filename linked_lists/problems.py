"""Linked-list practice problems ordered from easy to medium.

Complete these without looking at solutions.py. Focus on drawing the nodes and
arrows before writing code.
"""

from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    """Reverse a singly linked list and return its new head.

    LeetCode 206 - Easy

    Example:
        1 -> 2 -> 3 -> None becomes 3 -> 2 -> 1 -> None
    """
    pass


def has_cycle(head: ListNode | None) -> bool:
    """Return True if the linked list contains a cycle.

    LeetCode 141 - Easy

    A cycle exists when following next pointers eventually visits the same node
    again. Solve this with O(1) extra space.
    """
    pass


def merge_two_sorted_lists(
    list1: ListNode | None, list2: ListNode | None
) -> ListNode | None:
    """Merge two sorted linked lists and return the merged sorted list.

    LeetCode 21 - Easy

    Reuse the existing nodes instead of copying their values into a Python list.
    """
    pass


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    """Remove the nth node from the end and return the list's head.

    LeetCode 19 - Medium

    The list contains at least one node, and n is always valid. Try to solve it
    in one pass.
    """
    pass


def add_two_numbers(
    list1: ListNode | None, list2: ListNode | None
) -> ListNode | None:
    """Add two numbers stored in reverse-order linked lists.

    LeetCode 2 - Medium

    Each node contains one digit. Return the sum as a new reverse-order linked
    list, including a final carry when necessary.
    """
    pass
