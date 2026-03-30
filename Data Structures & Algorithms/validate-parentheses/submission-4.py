class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        

        match_pair = {'(':')', '[':']', '{':'}'}
        stack = []

        for b in s:
            if b in match_pair:
                stack.append(b)
            else:
                if not stack or b != match_pair[stack[-1]]:
                    return False
                stack.pop()

        return len(stack) == 0