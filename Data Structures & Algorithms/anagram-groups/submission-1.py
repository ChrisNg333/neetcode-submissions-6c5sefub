class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for word in strs:
            key = str(sorted(word))
            hmap[key].append(word)

        return list(hmap.values())