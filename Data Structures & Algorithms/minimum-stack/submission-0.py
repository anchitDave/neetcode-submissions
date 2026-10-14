class MinStack:

    def __init__(self):
        self.curr_min = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curr_min.append(min(val, self.curr_min[-1]) if self.curr_min else val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.curr_min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.curr_min[-1]
        
