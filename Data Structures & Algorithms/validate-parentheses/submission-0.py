class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if (len(stack) == 0):
                    return False
                c_top = stack.pop()
                if (c_top == "(" and c != ")") or (c_top == "[" and c != "]") or (c_top == "{" and c != "}"):
                    return False
        
        return (len(stack) == 0)