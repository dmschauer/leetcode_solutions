class Solution:
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0,len(nums)):
            remaining = target - nums[i]
            if(remaining in d.keys()):
                return [i,d[remaining]]
            d[nums[i]] = i
        