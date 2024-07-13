# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It is possible just to iterate through two linked lists simultaneously using two pointers, comparing elements on each iteration and adding them in the result linked list in the appropriate order.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Add elemets to the result linked list after comparison on every iteration, while there are elements in one of the start linked lists at least.
2. Add all elements from the left linked list to the result one.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, because it is done less than $N$ comparisons to build the result linked list.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity will be $O(N)$, where $N$ is the total size(number of elements) of the result linked list.

# Code
```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
        if list2 is not None:
            current.next = list2
        else:
            current.next = list1
        return head.next
```