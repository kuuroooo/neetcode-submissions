
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for x in strs:
            c = tuple(sorted(Counter(x).items()))
            if c in h:
                h[c].append(x)
            else:
                h[c] = [x]
        return list(h.values())