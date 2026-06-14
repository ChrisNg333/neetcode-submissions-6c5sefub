
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        olds = {}    #keep track of old nodes 
        olds[node] = Node(node.val) #start out with the current node
        q = deque([node])
        
        while q:
            curr = q.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in olds:
                    olds[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                olds[curr].neighbors.append(olds[neighbor])

        return olds[node]

