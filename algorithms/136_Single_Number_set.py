class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        set_sum = sum(set(nums))
        
        return 2*set_sum - nums_sum