class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum, curr = 0, 0
        for i in range(len(nums)):
            if nums[i] != 1:
                curr = 0
            if nums[i] == 1:
                curr +=1
            maximum = max(maximum, curr)
        return maximum