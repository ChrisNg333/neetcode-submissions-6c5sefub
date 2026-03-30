class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0],x[1]))
        #ans = []
        stack = []

        for cur in intervals:
            if stack and cur[0] <= stack[-1][1]:
                stack[-1][1] = max(cur[1], stack[-1][1])
            else:
                stack.append(cur)
        

        return stack

        