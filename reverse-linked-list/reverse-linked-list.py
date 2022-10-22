# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # iteratively
        current = head
        nodes = []
        while current:
            nodes.append(current.val)
            current = current.next
        
        current = head
        while current:
            current.val = nodes.pop()
            current = current.next
            
        return head