class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        #helper func to get the neighbor of curr node
        def neighbor(lock) -> list:
            res = []
            for i in range(4):
                #move forward
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                
                #move backward
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        q = deque()
        q.append(["0000",0])        # lock:turns
        visited = set(deadends)

        while q:
            lock, turns = q.popleft()
            
            if lock == target:
                return turns

            for nei in neighbor(lock):
                if nei not in visited:
                    visited.add(nei)
                    q.append([nei, turns + 1])

        return -1       #if reach here means no way to target
