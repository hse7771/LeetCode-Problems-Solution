from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_result = ListNode()
        current1, current2 = l1, l2
        current = l_result
        transit = 0
        while current1 and current2:
            current_result = current1.val + current2.val + transit
            current.val = current_result % 10
            transit = int(current_result >= 10)
            if current1.next or current2.next:
                current.next = ListNode()
                current = current.next
            current1, current2 = current1.next, current2.next
        current1 = current1 or current2
        while current1:
            current_result = current1.val + transit
            current.val = current_result % 10
            transit = int(current_result >= 10)
            if current1.next:
                current.next = ListNode()
                current = current.next
            current1 = current1.next
        if transit:
            current.next = ListNode(1)
        return l_result
