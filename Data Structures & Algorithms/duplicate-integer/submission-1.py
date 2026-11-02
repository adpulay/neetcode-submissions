class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for x in nums:
            if x not in seen:
                seen.append(x)
            elif x in seen:
                return True
        return False