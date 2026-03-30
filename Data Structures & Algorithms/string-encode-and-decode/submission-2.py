class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""        
        for s in strs:
            res += str(len(s))+"^"+s

        return res

    def decode(self, s: str) -> List[str]:
        res, i  = [], 0

        while i < len(s):
            j = i
            #move j to '^' location
            while s[j] != '^':
                j += 1
            #get len of word
            leng = int(s[i:j])
            res.append(s[j+1 : j + leng + 1])
            i = j + leng + 1

        return res
