class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,  cols = len(grid), len(grid[0])
        INF = 2**31 - 1
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: #if treasure
                    q.append((r,c))

        steps = 1
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()  #gets the coordinate

                for dx, dy in directions:
                    nx, ny = dx + x, dy + y

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == INF:
                        q.append((nx,ny))
                        grid[nx][ny] = steps

            
            steps += 1
                        

        
        
        


        
        
