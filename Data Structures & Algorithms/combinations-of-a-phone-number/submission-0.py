class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        dial_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []
        path = []

        def dfs(digits_index): # [3, 4]
            if digits_index == len(digits):
                res.append(''.join(path))
                return
            
            options = dial_map[digits[digits_index]]

            for option in options: #[d e f]
                path.append(option)
                dfs(digits_index+1)
                path.pop()
            
            return
        
        dfs(0)

        return res
