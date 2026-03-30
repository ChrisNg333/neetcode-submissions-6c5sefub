class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0]*len(temp)
        stack = [] # [temp , index]
        
        for i, curr_t in enumerate(temp):
            while stack and curr_t > stack[-1][0]:
                t, idx = stack.pop()
                res[idx] = (i - idx)
            stack.append([curr_t,i])

        return res 