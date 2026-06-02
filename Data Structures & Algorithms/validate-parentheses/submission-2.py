class Solution:
    def isValid(self, s: str) -> bool:
        compliment = {
            "(" : ")", 
            "{" : "}",
            "[" : "]",

        }
        opens = {"(" , "{" , "["}
        close = {"}" , ")" , "]"}
        stack = []
        for b in s:
            if b in opens:
                stack.append(b)
            else:
                if not stack:
                    return False
                elif compliment[stack[-1]] == b:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0