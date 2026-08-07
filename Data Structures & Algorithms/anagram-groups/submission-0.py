class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for ch in strs:
            count = [0]*26
            for l in ch:
                count[ord(l) - ord("a")] += 1
            table[tuple(count)].append(ch)
        return list(table.values())