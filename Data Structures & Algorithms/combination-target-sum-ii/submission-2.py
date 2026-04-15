class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def explore(path, start, cur):
            if cur == target:
                res.append(path[:])
                return 

            if cur > target:
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue

                path.append(candidates[i])

                explore(path, i + 1, cur + candidates[i])

                path.pop()      #backtrack

        explore([],0,0)

        return res
