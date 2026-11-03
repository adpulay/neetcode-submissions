class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, x in enumerate(nums):
            dtarg = target - x
            if dtarg in diff:
                return[diff[dtarg], i]
            diff[x] = i
        return []
        