# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list = 0

        cur = head

        while cur:
            len_list += 1
            cur = cur.next
        
        delete_node_index = len_list - n

        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head

        for i in range(delete_node_index):
            cur = cur.next
        
        cur.next = cur.next.next

        return dummy_head.next
