class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_len = 1
        cur_len = 0
        start = 0
        visited = dict()

        for i in range(0, len(s)):
            if s[i] not in visited.keys():
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                start = max(visited[s[i]], start)
                cur_len = i - start
                start = visited[s[i]] + 1 if visited[s[i]] > start else start
                
            visited[s[i]] = i
        
        return max(max_len, cur_len)
