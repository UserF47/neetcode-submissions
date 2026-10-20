"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 0(3) -> 1(2) -> 2(1) -> 3(0) -> None
# key: old_0
# value: new_0, new_3 points to hashmap[old_0] -> new_0

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        node_map = {}
        dummy_head = Node(0)
        copy_head = Node(0)
        dummy_head.next = copy_head

        cur=head

        while cur:
            copy_head.val = cur.val
            if cur.next:
                copy_head.next = Node(0)

            node_map[cur] = copy_head
            copy_head.random = cur.random

            cur = cur.next
            copy_head = copy_head.next

        cur = dummy_head.next

        while cur:
            cur.random = node_map[cur.random] if cur.random else None
            cur = cur.next

        return dummy_head.next
