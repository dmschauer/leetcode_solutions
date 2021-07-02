import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = []        
        
        for i in range(0,len(points)):
            dist.append(math.sqrt(points[i][0]**2 + points[i][1]**2))
            
        dist_sorted = dist.copy()
        dist_sorted.sort()  
        max_dist = dist_sorted[k-1]
                             
        result = []
        for i in range(0,len(points)):
            if(dist[i] <= max_dist):
                result.append(points[i])
                                
        return result