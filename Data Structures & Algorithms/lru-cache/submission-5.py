class Node:

    def __init__(self, key=-1, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap_node = {} #{key: node}

        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.nxt = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head


    def get(self, key: int) -> int:
        if key in self.hashmap_node:
            node_update = self.hashmap_node[key]
            self.delete_node(node_update)

            self.add_node(node_update)
            # self.hashmap_node[key] = node_update

            return node_update.val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if not key in self.hashmap_node: # new key
            node_new = Node(key, value)
            self.add_node(node_new)
            self.hashmap_node[key] = node_new

            if len(self.hashmap_node) > self.capacity:
                node_remove = self.dummy_head.nxt
                self.delete_node(node_remove)
                del self.hashmap_node[node_remove.key]
        else:
            node_update = self.hashmap_node[key]
            self.delete_node(node_update)

            node_update.val = value
            self.add_node(node_update)
            # self.hashmap_node[key] = node_update

    def delete_node(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
    
    def add_node(self, node_new):

        self.dummy_tail.prev.nxt = node_new
        node_new.prev = self.dummy_tail.prev
        self.dummy_tail.prev = node_new
        node_new.nxt = self.dummy_tail
        



        
