# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head

        fast = dummy_node
        for i in range(n):
            fast = fast.next
        
        slow = dummy_node
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy_node.next 
