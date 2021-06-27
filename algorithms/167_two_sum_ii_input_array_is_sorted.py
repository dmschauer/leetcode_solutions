# The key insight is that you can take advantage of the pre-sorted array by using pointers
# at the beggining and end of the array.
#
# Because the array is sorted, you can move the left pointer to the right (+1) to increase
# the sum of the two values the pointers are pointing to. 
# Similarily, because the array is sorted, you can move the right pointer to the left (-1)
# to decrease the sum of the two values the pointers are pointing to. 
# 
# In the worst case you will alternate between shifting the left and right pointer towards the
# center of the array until you have reached the very center of it. 
# In any case, using "while True" is save here, because by definition there is a solution
# present in the numbers array. If there wasn't this guarantee, you might use
# "while left < right" instead to avoid unnecessary checks and index out of range exceptions.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while True: 
            current_sum = numbers[left] + numbers[right]
            if(current_sum == target):
                return((left+1, right+1));
            elif(current_sum < target):
                left += 1;
            else:
                right -= 1;