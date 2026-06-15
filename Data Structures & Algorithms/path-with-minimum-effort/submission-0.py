class Solution:
    def minimumEffortPath(self, h: List[List[int]]) -> int:
        rows,cols = len(h), len(h[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()     #[r,c]

        minheap = [[0,0,0]]        #[effort, r, c]

        while minheap:
            cur_effort, r, c = heapq.heappop(minheap)           #smallest effort popped
            if (r,c) in visited:
                continue

            visited.add((r,c))
            if r == rows-1 and c == cols-1:
                return cur_effort       #found          

            for dx, dy in directions:
                nx, ny = dx + r, dy + c
                if 0 <= nx < rows and 0 <= ny < cols and (nx,ny) not in visited: 
                    new_effort = max(cur_effort, abs(h[r][c] - h[nx][ny]))                
                    heapq.heappush(minheap,[new_effort, nx, ny])


            

