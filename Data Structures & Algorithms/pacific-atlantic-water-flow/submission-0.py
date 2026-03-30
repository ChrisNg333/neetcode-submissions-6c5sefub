class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        rows, cols = len(h), len(h[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev):
            if  r < 0 or r >= rows or c >= cols or c < 0 or (r,c) in visited or h[r][c] < prev:
                return         
            
            visited.add((r,c))
            dfs(r-1, c, visited, h[r][c])
            dfs(r, c-1, visited, h[r][c])
            dfs(r+1, c, visited, h[r][c])
            dfs(r, c+1, visited, h[r][c])

        for r in range(rows):
            dfs(r, 0, pacific, h[r][0]) #check if left can flow to Alantic
            dfs(r, cols-1, atlantic, h[r][cols-1] )

        for c in range(cols):
            dfs(0, c, pacific, h[0][c])
            dfs(rows - 1, c, atlantic, h[rows-1][c])
    

        return list(atlantic & pacific)