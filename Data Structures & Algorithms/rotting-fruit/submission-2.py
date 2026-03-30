class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        q = deque()
        fresh = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:     #if rotten, add to q
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                x,y  = q.popleft()

                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    
                    #only affect the fresh one 
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append([nx,ny])
                        
            time += 1

        return time if fresh == 0 else -1

