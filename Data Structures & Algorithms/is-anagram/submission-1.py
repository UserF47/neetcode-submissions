class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)

        for c in s:
            counter[c] += 1
        
        for c in t:
            counter[c] -= 1

        for _, val in counter.items():
            if val != 0:
                return False
        
        return True