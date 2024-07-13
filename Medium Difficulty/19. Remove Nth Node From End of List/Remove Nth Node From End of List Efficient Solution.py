from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        if length == 1 and n == 1:
            return
        if length == n:
            return head.next
        current = head
        current_i = 0
        while current.next and current_i != length - n - 1:
            current = current.next
            current_i += 1
        current.next = current.next.next
        return head
