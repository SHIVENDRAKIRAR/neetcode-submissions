class Solution:
    def isValid(self, s: str) -> bool:
        compliment = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for b in s:
            if b in compliment:
                stack.append(b)
            elif stack and compliment[stack[-1]] == b:
                stack.pop()
            else:
                return False

        return not stack