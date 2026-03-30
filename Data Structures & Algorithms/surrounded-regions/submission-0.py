class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board) , len(board[0])
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]

        #takes in coor and turn 'O' to '#'

        def bfs(row,col):
            q = deque()
            q.append((row,col))

            while q:
                r, c = q.popleft()
                board[r][c] = '#'   #marked

                for dx, dy in directions:
                    nx, ny = r + dx, c + dy

                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'O':
                        board[nx][ny] = '#'
                        q.append((nx, ny))
        
        # bfs all the edges 'O'
        for i in range(cols):
            if board[0][i] == 'O':
                bfs(0,i)
            if board[rows-1][i] == 'O':
                bfs(rows-1,i)

        for i in range(rows):
            if board[i][0] == 'O':
                bfs(i,0)
            if board[i][cols-1] == 'O':
                bfs(i,cols-1)

        
        # run through matrix again to convert
        for r in range(rows):
            for c in range(cols): 
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
            