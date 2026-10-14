class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']

        def calculate(i, j, op):
            if op == '+':
                return i+j
            elif op == '-':
                return i-j
            elif op == '*':
                return i*j
            elif op == '/':
                return int(i/j)

        for i in range(len(tokens)):
            if tokens[i] in op:
                r = stack.pop()
                l = stack.pop()
                stack.append(calculate(l, r, tokens[i]))
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]

        