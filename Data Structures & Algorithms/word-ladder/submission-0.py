class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        world_set = set(wordList)
        if not endWord in world_set:
            return 0

        q = deque([beginWord])
        level = 1
        visited = set([beginWord])

        while q:
            layer = deque()
            while q:
                word = q.popleft()
                word_length = len(word)
                for i in range(word_length):
                    for change in 'abcdefghijklmnopqrstuvwxyz':
                        after_change = word[:i] + change + word[i+1:]

                        if after_change == endWord:
                            return level + 1

                        if after_change in world_set and not (after_change in visited):
                            layer.append(after_change)
                            visited.add(after_change)
                
            while layer:
                q.append(layer.popleft())
                
            level += 1
            
        return 0