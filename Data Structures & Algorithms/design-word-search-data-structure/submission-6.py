class TreeNode():
    
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TreeNode()
            
            node = node.children[ch]
        
        node.is_end = True

    def search(self, word: str) -> bool:

        def dfs(node, word):
            if not word:
                return node.is_end
            
            if word[0] in node.children:
                return dfs(node.children[word[0]], word[1:])
            
            if word[0] != '.' and word[0] not in node.children:
                return False
            
            if word[0] == '.':
                for child in node.children.values():
                    if dfs(child, word[1:]):
                        return True
                return False


        return dfs(self.root, word)
        




