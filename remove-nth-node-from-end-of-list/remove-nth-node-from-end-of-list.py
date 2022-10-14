# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head
        right_prev = None
        for i in range(n-1):
            right = right.next
        while right.next:
            right_prev = right
            right = right.next
            left = left.next
        if left.next:
            left.val = left.next.val
            left.next = left.next.next
        else:
            if right_prev:
                right_prev.next = None
            else:
                return None
        return head