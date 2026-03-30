class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)] # 4 directions


        def bfs(r,c):
            q = deque()
            q.append([r,c])

            while q:
                row, col = q.popleft()

                for dx, dy in directions:
                    nr , nc = row + dx, col + dy
                    if 0 <= nr < rows and 0<= nc < cols and grid[nr][nc] == '1':
                        q.append([nr,nc])
                        grid[nr][nc] = '0' # mark as visited


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    position = (r,c)
                    bfs(r,c)
                    islands += 1

        
        return islands




            