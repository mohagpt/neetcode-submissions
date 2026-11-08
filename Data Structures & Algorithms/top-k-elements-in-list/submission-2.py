class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums : 
            count[n] = count.get(n, 0) + 1
        
        heap = []
        for n, count in count.items() : 
            heapq.heappush(heap, [-count, n])
        
        
        return [heapq.heappop(heap)[1] for _ in range(k)]

        
 
