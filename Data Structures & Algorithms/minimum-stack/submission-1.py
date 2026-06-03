class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.Min:
            if val <= self.Min[-1]:
                self.Min.append(val)
        else:
            self.Min.append(val)
        

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.Min[-1]:
            self.Min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.Min[-1]
        
