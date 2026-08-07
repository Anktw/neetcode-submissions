class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, ch in enumerate(nums):
          compliment = target - ch
          if compliment in table:
            return [table[compliment], i]
          table[ch] = i