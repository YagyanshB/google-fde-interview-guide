"""Annotated solutions for the linked-list practice problems."""

from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    """Reverse a singly linked list using three pointers."""
    previous = None
    current = head

    while current:
        next_node = current.next  # Save the rest before changing the arrow.
        current.next = previous  # Point the current node backward.
        previous = current  # Move previous to the node just reversed.
        current = next_node  # Continue through the original list.

    return previous


# Time: O(n) because every node is visited once.
# Space: O(1) because only pointer variables are used.


def has_cycle(head: ListNode | None) -> bool:
    """Detect a cycle with Floyd's slow and fast pointers."""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next  # Slow moves one node.
        fast = fast.next.next  # Fast moves two nodes.

        if slow is fast:  # Inside a cycle, fast eventually catches slow.
            return True

    return False


# Time: O(n) because the pointers move through at most a linear number of nodes.
# Space: O(1) because no set of visited nodes is needed.


def merge_two_sorted_lists(
    list1: ListNode | None, list2: ListNode | None
) -> ListNode | None:
    """Merge two sorted lists using a dummy node and a moving tail."""
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1  # Attach the smaller available node.
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next  # Move the end of the merged list forward.

    tail.next = list1 or list2  # One list may still have nodes remaining.
    return dummy.next


# Time: O(n + m) because each node from both lists is processed once.
# Space: O(1) because the existing nodes are reused.


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    """Remove the nth node from the end with a fixed pointer gap."""
    dummy = ListNode(0, head)
    slow = fast = dummy

    # Put n + 1 nodes between fast and slow. The extra step makes slow stop
    # immediately before the node that must be removed.
    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next  # Skip the target node.
    return dummy.next


# Time: O(n) because the list is traversed once.
# Space: O(1) because only two moving pointers and a dummy node are used.


def add_two_numbers(
    list1: ListNode | None, list2: ListNode | None
) -> ListNode | None:
    """Add reverse-order digits while carrying into the next place."""
    dummy = ListNode()
    tail = dummy
    carry = 0

    while list1 or list2 or carry:
        value1 = list1.val if list1 else 0
        value2 = list2.val if list2 else 0
        total = value1 + value2 + carry

        carry, digit = divmod(total, 10)
        tail.next = ListNode(digit)  # Build one result digit at a time.
        tail = tail.next

        if list1:
            list1 = list1.next
        if list2:
            list2 = list2.next

    return dummy.next


# Time: O(max(n, m)) because each input node is visited once.
# Space: O(max(n, m)) for the output list; O(1) auxiliary space.
