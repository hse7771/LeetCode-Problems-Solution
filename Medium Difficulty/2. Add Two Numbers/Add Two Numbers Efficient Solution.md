# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem is a bit more difficult than classic merging two linked lists problem.
The linked lists are numbers presented by separate digits in inverse order, so they can be summed without any additional manipulations. It is necessary to perform summing operation on each sequential pair of elements of given linked lists and add the result to the result linked list. 

# Approach
<!-- Describe your approach to solving the problem. -->
1. Iterate through the both of given linked lists performing necessary calculations.
2. Store the additional decimal place if it appears.
3. Add digits from the left linked list.
4. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the length of the result linked list, as no more than $N$ (sum of lengthes of given linked lists) merging iterations are performed to have the result linked list.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of the result linked list to store this list.
# Code
```
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
```