# By sorting the array we can subsequently check if two adjacent numbers
# in it have the same value (i.e. if they are duplicates)
# Obviously there's no need to go this far if there aren't at least two
# values in the array, since then it's impossible to have duplicates. 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) < 2):
            return False
        else:
            nums.sort()
        
        for i in range(0,len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True
            
        return False