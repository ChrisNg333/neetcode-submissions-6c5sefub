class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #build adjacency graph
        graph = {i:[] for i in range(numCourses)}
        for req in prerequisites: 
            graph[req[1]].append(req[0])

        #dfs    
        visited = set()
        def dfs(n):
            #if same n found while dfs
            if n in visited:
                return True #loop found

            if graph[n] == []:  #end of node (no prereq)
                return False

            visited.add(n)

            for pre in graph[n]:
                if dfs(pre):    #loop found
                    return True

            visited.remove(n)
            graph[n] = []
            return False

        for node in graph:
            if dfs(node):       # True = loop found
                return False    

        return True
