# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        next = current.next
        current.next = None
        
        while next:
            temp_next_next = next.next
            temp_next = next
            
            next.next = current
            
            current = temp_next
            next = temp_next_next
            
        return current