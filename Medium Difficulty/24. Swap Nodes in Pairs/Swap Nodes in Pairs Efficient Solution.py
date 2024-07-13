from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if head is None or head.next is None:
            return head
        tmp = current.next
        current.next = tmp.next
        tmp.next = current
        head = tmp
        while current and current.next and current.next.next:
            tmp = current.next
            current.next = tmp.next
            tmp.next = current.next.next
            current.next.next = tmp
            current = current.next.next
        return head
