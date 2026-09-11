class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        def countSubstringsHelper(left, right):
            nonlocal counter

            while left >= 0 and right < len(s) and s[left] == s[right]:
                counter += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            countSubstringsHelper(i, i)
            countSubstringsHelper(i, i+1)
        
        return counter
