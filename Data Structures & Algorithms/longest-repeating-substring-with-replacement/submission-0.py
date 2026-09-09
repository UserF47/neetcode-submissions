class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = [0] * 26
        max_len = 0
        left = 0
        max_freq = 0

        for i in range(len(s)):
            counter[ord(s[i])-ord("A")] += 1
            cur_len = i - left + 1
            max_freq = max(max_freq, counter[ord(s[i])-ord("A")])

            if cur_len - max_freq <= k:
                max_len = max(max_len, cur_len)
                continue
            
            counter[ord(s[left]) - ord("A")] -= 1
            left+=1
        
        return max_len

