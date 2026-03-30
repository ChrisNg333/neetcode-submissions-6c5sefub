class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols = len(board),len(board[0])
        col_set = [set() for _ in range(9)]
        row_set = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(rows):
            for c in range(cols):

                num = board[r][c]
                if num == ".":
                    continue        #ignore this symbol

                # for sub box
                box = (r//3)*3 + (c//3)     #calc box index
                if num in boxes[box]:
                    return False
                else: boxes[box].add(num)

                #for each row:
                if num in row_set[r]:
                    return False
                else: row_set[r].add(num)

                #for each col:
                if num in col_set[c]:
                    return False
                else: col_set[c].add(num)           
        

        return True

