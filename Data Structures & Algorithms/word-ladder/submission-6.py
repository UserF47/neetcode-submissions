from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list_set = set(wordList)

        steps = 1
        q = deque([beginWord])
        visited = {beginWord}

        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return steps

                for i in range(len(w)):
                    for change in 'abcdefghijklmnopqrstuvwxyz':
                        after = w[:i] + change + w[i+1:]

                        if after in word_list_set and after not in visited:
                            q.append(after)
                            visited.add(after)
            steps += 1
        
        return 0
                        
