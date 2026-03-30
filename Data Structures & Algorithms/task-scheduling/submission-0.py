class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        time = 0
        heap = [-n for n in count.values()]       #maxheap 
        heapq.heapify(heap)        
        q = deque()     #store pair [-num, time]

       
        while heap or q:
            time += 1
            if heap:
                num = 1 + heapq.heappop(heap)   # subtract one task, +1 in this case 
                if num:
                    q.append([num,time + n])    
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])


        return time