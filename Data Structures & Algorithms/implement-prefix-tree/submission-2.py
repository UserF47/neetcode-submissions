class TreeNode:

    def __init__(self): 
        self.children = {}
        self.end_word = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        # "dog"
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TreeNode()

            node = node.children[ch]
        
        node.end_word = True


    def search(self, word: str) -> bool:
        # "dog"
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]
        
        return node.end_word

    def startsWith(self, prefix: str) -> bool:
        # "dog"
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False

            node = node.children[ch]
        
        return True

        