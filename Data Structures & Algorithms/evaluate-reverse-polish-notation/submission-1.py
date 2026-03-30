class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c.lstrip('-').isdigit():
                stack.append(int(c))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if c == '+':
                    stack.append(num1 + num2)
                elif c == '-':
                    stack.append(num1 - num2)
                elif c == '*':
                    stack.append(num1 * num2)
                elif c == '/':
                    stack.append(int(num1/num2))

        return stack.pop()