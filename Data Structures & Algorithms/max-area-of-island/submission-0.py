class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        maxArea = 0
        
        
        def bfs(x, y):           
            q = deque([(x, y)])
            area = 0
            grid[x][y] = 0 # mark as visited

            while q:
                pt = q.popleft()
                area += 1

                for dx, dy in directions:
                    nx, ny = pt[0] + dx, pt[1] + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 :#if another valid island
                        q.append([nx, ny])
                        grid[nx][ny] = 0 #mark as visited 
                        
            return area
                 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea,bfs(i,j))

        return maxArea


