class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        size = len(temperatures)
        res = [0] * size

        for i in range(size):
            # if not stack:
            #     stack.append(i)
            # else:
            #     if temperatures[stack[-1]] >= temperatures[i]:
            #         stack.append(i)
            #     else:
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                res[top] = i - top

            stack.append(i)

        return res