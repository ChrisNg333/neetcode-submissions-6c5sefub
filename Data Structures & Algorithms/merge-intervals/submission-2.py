class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key= lambda x: x[0])      #sort by start 

        stack = []    #stack       
        for interval in intervals:
            if stack and interval[0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], interval[1])
                continue
                
            stack.append(interval)
        
        return stack