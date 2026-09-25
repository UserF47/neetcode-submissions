class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)

        left = 0
        right = len(s) - 1

        while left < right:
            while left <= length - 1 and (not s[left].isalnum()):
                left += 1
            
            while right > -1 and (not s[right].isalnum()):
                right -= 1
            
            
            if not (left < right):
                break

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        
        return True