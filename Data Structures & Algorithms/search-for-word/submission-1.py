class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board), len(board[0])
        directions = [(0,1), (1,0) , (0,-1), (-1, 0)]

        def explore(indx, x , y):   #using dfs
            if board[x][y] != word[indx]:
                return False
            
            if indx == len(word)-1:
                return True

            

            temp = board[x][y]
            board[x][y] = '#'   #mark as visited

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if explore (indx + 1, nx, ny):
                        return True
            
            board[x][y] = temp  #return old value
            return False


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if explore(0,i,j):
                        return True

        
        return False