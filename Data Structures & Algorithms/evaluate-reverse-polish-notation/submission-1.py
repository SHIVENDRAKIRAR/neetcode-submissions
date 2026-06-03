class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+" , "-" , "*" , "/"}
        s = []
        for ch in tokens:
            if ch == "+":
                a = s.pop()
                b = s.pop()
                x = a + b
                s.append(x)
            elif ch == "-":
                a = s.pop()
                b = s.pop()
                x = b - a
                s.append(x)
            elif ch == "*":
                a = s.pop()
                b = s.pop()
                x = a * b
                s.append(x)                                 
            elif ch == "/" :
                a = s.pop()
                b = s.pop()
                x = int(b/a)
                s.append(x)  
            else:
                s.append(int(ch))
        return int(s[0])              
            
                

