# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0,1,2,3]
# None->0->1->2->3->None

# None<-0<-1<-2<-3<-None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      prev, cur = None, head

      while cur:
        nxt = cur.next
        cur.next = prev

        prev = cur
        cur = nxt
    
      return prev
