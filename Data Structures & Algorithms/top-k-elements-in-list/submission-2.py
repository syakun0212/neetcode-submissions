class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)

        heap = [] 
        for value, freq in count.items():
            heapq.heappush(heap, [freq, value])
            if len(heap) > k:
                heapq.heappop(heap)
     
       # print results  
        res = []
        while k > 0 and heap: 
            freq, value = heapq.heappop(heap)
            res.append(value)

        return res 

