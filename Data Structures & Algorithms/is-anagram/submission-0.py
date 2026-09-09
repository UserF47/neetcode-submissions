class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}

        for char in s:
            if not char in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        
        for char in t:
            if not char in counter:
                return False
            else:
                counter[char] -= 1
        
        for char in counter.keys():
            if counter[char] != 0:
                return False
        
        return True