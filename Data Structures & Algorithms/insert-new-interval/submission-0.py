class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:
            #curr interval is completely before newIntval
            if interval[1] < newInterval[0]:
                res.append(interval)

            #curr interval is completely behind newIntval
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval

            #overlap occurs, dont append but change the newInterval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        res.append(newInterval)
        return res
        


        