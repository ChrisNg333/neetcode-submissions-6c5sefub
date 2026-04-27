class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                if r == 0:
                    grid[0][c] += grid[0][c-1]
                elif c == 0:
                    grid[r][0] += grid[r-1][0]
                else:
                    grid[r][c] += min(grid[r-1][c],grid[r][c-1])
        

        return grid[rows-1][cols-1]