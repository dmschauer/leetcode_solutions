# By using a dictionary to remember each value we had seen before, 
# we will know in case we encounter the same value a second time (i.e. it's a duplciate)
     
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        
        for num in nums: 
            if num in num_dict:
                return True
            else:
                num_dict[num] = None
                
        return False