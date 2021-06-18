class Solution:
    
    def reverse(self, x: int) -> int:
        max_int = 2**31 - 1
        min_int = 2**31 * -1 
                        
        # reverse unsigned integer
        # casting back to integer also removes possible leading 0s
        if (x < 0):
            x = -1 * x
            x = int(str(x)[::-1]) * -1
        else:
            x = int(str(x)[::-1])
            
        if (x <= max_int or x >= max_int):
            return 0
        else:
            return x                   