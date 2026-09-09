class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        stack = []

        for t in tokens:
            if not t in ops:
                stack.append(int(t))
            else:
                right=stack.pop()
                left=stack.pop()
                if t == '+':
                    res = left + right
                elif t == '-':
                    res = left - right
                elif t == '*':
                    res = left * right
                else:
                    res = int(left / right)
                
                stack.append(res)
        
        return stack[0]
