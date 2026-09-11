class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def longestPalindromeHelper(left, right):
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left+1, right-1
        
        for i in range(len(s)):
            left, right = longestPalindromeHelper(i, i)
            if len(s[left:right+1]) > len(res):
                res = s[left:right+1]
            
            left, right = longestPalindromeHelper(i, i+1)
            if len(s[left:right+1]) > len(res):
                res = s[left:right+1]

        return res