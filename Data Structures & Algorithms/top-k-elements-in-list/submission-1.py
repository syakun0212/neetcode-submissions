class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = collections.Counter(nums)
        
        maxHeap = []
        for i, v in count.items(): 
            maxHeap.append([v,i])

        heapq.heapify_max(maxHeap)

        res = [] 
        while k > 0:
            if maxHeap:
                freq, value = heapq.heappop_max(maxHeap)
                res.append(value)
            k -= 1
        
        return res 

         