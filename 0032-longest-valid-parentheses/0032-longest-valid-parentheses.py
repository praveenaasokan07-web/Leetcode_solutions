class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]   # base index
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                
                if not stack:
                    # no base to calculate length
                    stack.append(i)
                else:
                    # valid substring length
                    max_length = max(max_length, i - stack[-1])

        return max_length
