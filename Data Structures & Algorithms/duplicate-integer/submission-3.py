class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()

        for i in range(len(nums)):
            duplicates.add(nums[i])

        if len(duplicates) != len(nums):
            return True
        else:
            return False