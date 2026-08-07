class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        freq = [[] for _ in range(len(nums)+1)]
        for n in nums:
            table[n] = table.get(n, 0) + 1
        for n, c in table.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            