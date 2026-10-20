# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        len_list = 0

        cur = head
        while cur:
            len_list += 1
            cur = cur.next
        
        mid = len_list // 2

        forward_head = head

        forward_counter = mid
        cur = head

        for i in range(mid):
            cur = cur.next

        backward_head = cur.next
        cur.next = None

        # reverse backward_head

        prev, cur = None, backward_head

        while cur:
            nxt = cur.next
            
            cur.next = prev
            prev = cur
            cur = nxt

        backward_head = prev

        # merge two list

        merged_head = ListNode()
        merged_head_cur = merged_head
        step = 0

        while forward_head and backward_head:
            if step % 2 == 0:
                merged_head_cur.next = forward_head
                forward_head = forward_head.next
            else:
                merged_head_cur.next = backward_head
                backward_head = backward_head.next
            
            step += 1
            merged_head_cur = merged_head_cur.next
        
        if forward_head:
           merged_head_cur.next = forward_head
        
        if backward_head:
           merged_head_cur.next = backward_head





        