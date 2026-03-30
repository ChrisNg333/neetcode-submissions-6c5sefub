class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p, s) for p, s in zip(position, speed)], reverse = True)
        fleets = 0
        stack = []


        for pos, spd in cars:
            time = (target - pos) / spd
            
            if not stack or time > stack[-1]: # if empty and time is different
                # new fleet
                fleets += 1
                stack.append(time)

        return fleets






        