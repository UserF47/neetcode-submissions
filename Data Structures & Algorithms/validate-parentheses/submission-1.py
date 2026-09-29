class Solution:
    def isValid(self, s: str) -> bool:
        c_map = {')': '(', '}': '{', ']': '['}

        stack = []

        for c in s:
            if stack and c in c_map:
                top = stack.pop()
                if top != c_map[c]:
                    return False
            else:
                stack.append(c)
        
        return False if stack else True
            