class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # if stack empty and close parentheses 
            if not stack and c in "})]":
                return False
            
            if c in "{([":
                stack.append(c)
            else: 
                if c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                else: 
                    return False


        return True if len(stack) == 0 else False