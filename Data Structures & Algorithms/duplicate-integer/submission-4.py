class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = -1
        for value in nums:
            if prev == value: 
                return True
            prev = value
        return False;

        