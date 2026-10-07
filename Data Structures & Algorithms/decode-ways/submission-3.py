class Solution:
    def numDecodings(self, s: str) -> int:
        prev_2 = 1
        prev_1 = 1 if s[0] != '0' else 0

        for i in range(1, len(s)):
            cur = 0
            if s[i] != '0':
                cur += prev_1
            
            if 10 <= int(s[i-1: i+1]) <= 26:
                cur += prev_2

            prev_2 = prev_1
            prev_1 = cur
        
        return prev_1