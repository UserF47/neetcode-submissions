class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = ""

        for ele in s:
            if ele.isalpha():
                s_alpha += ele.lower()
            elif ele.isdigit():
                s_alpha += ele
            else:
                continue
        
        if len(s_alpha) < 2:
            return True
        
        i = 0
        j = len(s_alpha) - 1

        while i < j:
            if s_alpha[i] != s_alpha[j]:
                return False
            
            i += 1
            j -= 1
        
        return True