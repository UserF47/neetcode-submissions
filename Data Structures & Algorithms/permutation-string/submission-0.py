class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        need = [0] * 26
        have = [0] * 26
        m = len(s1)

        for i in range(m):
            need[ord(s1[i]) - ord('a')] += 1
            have[ord(s2[i]) - ord('a')] += 1
        
        if need == have:
            return True
        
        for i in range(m, len(s2)):
            have[ord(s2[i]) - ord('a')] += 1
            have[ord(s2[i-m]) - ord('a')] -= 1

            if need == have:
                return True
        
        return False