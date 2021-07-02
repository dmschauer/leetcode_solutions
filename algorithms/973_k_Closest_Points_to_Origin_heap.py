import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        for x,y in points:
            minHeap.append([x**2 + y**2, x ,y]) # no need for sqrt for comparing distances
        
        # sorts elements in dist by first index (calculated distance)
        heapq.heapify(minHeap)
        
        result = []
        
        for i in range(0,k):
            d, x, y = heapq.heappop(minHeap)
            result.append([x,y])
            
        return result