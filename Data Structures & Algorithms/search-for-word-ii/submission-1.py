class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows,cols = len(board), len(board[0])

        #buidl the tree from matrix
        root = TrieNode()       #original point

        for word in words:
            node = root 
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word        #save the word
        #DFS 
        visited = set()
        res = set()
        def dfs(r, c, node):
            if (
                r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                (r,c) in visited
            ):
                return 

            ch = board[r][c]

            if ch not in node.children:
                return 
            
            nextnode = node.children[ch]
            if nextnode.word:       #found a word 
                res.add(nextnode.word)
            
            visited.add((r,c))

            dfs(r+1, c, nextnode)
            dfs(r, c+1, nextnode)
            dfs(r-1, c, nextnode)
            dfs(r, c-1, nextnode)

            visited.remove((r,c))

        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)

        return list(res)


















