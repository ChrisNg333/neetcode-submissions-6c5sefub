class Solution:
    def makesquare(self, matches: List[int]) -> bool:
        total = sum(matches)


        if total % 4 != 0:
            return False

        target = total // 4
        matches.sort(reverse=True)

        if matches[0] > target:     #one side break the rule
            return False    

        side = [0, 0 , 0, 0]        #represent 4 sides

        def dfs(i):
            if i == len(matches):
                return True 

            for j in range(4):
                if matches[i] + side[j] <= target:
                    side[j] += matches[i]

                    if dfs(i+1):
                        return True     

                    side[j] -= matches[i]



            return False


        return dfs(0)
            
