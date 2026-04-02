class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        if not h:
            return 0

        stack = []  #store [start_index : height]
        res = 0     #max area

        for i in range(len(h)):
            start = i   #to see how far left u can extend 
            while stack and h[i] < stack[-1][1]:
                idx, height = stack.pop()
                area = (i - idx) * height
                res = max(res, area)
                start = idx
            
            stack.append([start, h[i]])
            

        while stack:
            i, height = stack.pop()
            w = len(h) - i
            res = max(res, w*height)

        return res
