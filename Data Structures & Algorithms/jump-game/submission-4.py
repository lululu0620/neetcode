class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = 0
        for i, step in enumerate(nums):
            if i > canReach:
                break
            canReach = max(canReach, i + step)
            if canReach >= len(nums) - 1:
                return True
        return False

        
