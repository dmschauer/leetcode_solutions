from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt_dict = defaultdict(int)
        
        for num in nums: 
            cnt_dict[num] += 1
            
        for num in cnt_dict:
            if cnt_dict[num] == 1:
                return num