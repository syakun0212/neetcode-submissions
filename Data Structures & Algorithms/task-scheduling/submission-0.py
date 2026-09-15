class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [i for i in count.values()]
        heapq.heapify_max(maxHeap)

        time = 0
        q = deque() 
        while maxHeap or q:
            time += 1 
            if maxHeap:
                count = heapq.heappop_max(maxHeap) -1 
                if count > 0:
                    q.append([count, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])
        
        return time 