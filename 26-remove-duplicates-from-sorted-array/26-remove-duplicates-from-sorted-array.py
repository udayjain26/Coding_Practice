class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        nums[:]=sorted(list(s))
        return len(nums)
        