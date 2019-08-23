class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 树形结构
        #   a     b
        #  /|\   /|\
        # d e f d e f
        num_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                   '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []

        def backtrack(tmp, next_digits):
            if len(next_digits) == 0:
                ans.append(tmp)
            else:
                for c in num_map[next_digits[0]]:
                    backtrack(tmp + c, next_digits[1:])

        if len(digits) > 0:
            backtrack('', digits)
        return ans


