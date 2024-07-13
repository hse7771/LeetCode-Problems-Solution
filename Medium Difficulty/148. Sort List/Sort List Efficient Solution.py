from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(head1, head2):
            head_common = ListNode()
            current = head_common
            while head1 and head2:
                if head1.val < head2.val:
                    current.next = head1
                    head1 = head1.next
                else:
                    current.next = head2
                    head2 = head2.next
                current = current.next
            current.next = head1 or head2
            return head_common.next

        def find_middle(head):
            middle = head
            fast_middle = head
            while fast_middle.next and fast_middle.next.next:
                middle = middle.next
                fast_middle = fast_middle.next.next
            head = middle.next
            middle.next = None
            return head

        if not head or not head.next:
            return head

        head1 = head
        head2 = find_middle(head)

        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return merge(head1, head2)
