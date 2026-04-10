class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            while stack and stack[-1] > 0 and num < 0:    #if ollision happen
                if abs(num) > stack[-1]:
                    stack.pop()
                    continue        # to break the loop and add the new asteroid
                elif abs(num) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(num)

        return stack