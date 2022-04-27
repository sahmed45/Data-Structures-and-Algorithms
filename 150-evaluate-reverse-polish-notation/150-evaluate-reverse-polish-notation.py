class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                stack.append(-stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                stack.append(int((1/stack.pop()) * stack.pop()))
            else:
                stack.append(int(c))
        return stack.pop()