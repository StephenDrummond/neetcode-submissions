class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        operators = {
            '+': lambda b, a: a + b,
            '-': lambda b, a: a - b,
            '*': lambda b, a: a * b,
            '/': lambda b, a: int(a/b)
        }
        
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                res = operators[t](stack.pop(), stack.pop())
                stack.append(res)
        return stack[0]