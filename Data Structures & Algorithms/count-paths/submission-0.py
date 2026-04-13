class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        graph = [[1]*cols for _ in range(rows)]

        for r in range(1,rows):
            for c in range(1,cols):
                curr = graph[r-1][c] + graph[r][c-1]
                graph[r][c] = curr


        return graph[rows-1][cols-1]

        