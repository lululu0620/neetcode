class Solution:
    def jump(self, nums: List[int]) -> int:
        canReach, times, curr = 0, 0, 0
        for i, step in enumerate(nums):
            if i == len(nums) - 1:
                break
            canReach = max(canReach, i + step)
            if i == curr:
                curr = canReach
                times += 1
        return times