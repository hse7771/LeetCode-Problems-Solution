from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        if length == 0:
            return
        k %= length

        tail, new_tail = head, head
        count = 0
        while tail:
            if tail.next is None:
                break
            else:
                count += 1
                tail = tail.next
                if count == k + 1:
                    new_tail = new_tail.next
                    count = k
        tail.next = head
        head = new_tail.next
        new_tail.next = None
        return head
