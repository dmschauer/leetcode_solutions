# By using a dictionary to remember each value we had seen before, 
# we will know in case we encounter the same value a second time (i.e. it's a duplciate)
# Obviously there's no need to go this far if there aren't at least two
# values in the array, since then it's impossible to have duplicates. 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) < 2):
            return False
        
        value_dict = {}
        
        for i in range(0,len(nums)):
            if(nums[i] in value_dict):
                return True
            else:
                value_dict[nums[i]] = None
            
        return False