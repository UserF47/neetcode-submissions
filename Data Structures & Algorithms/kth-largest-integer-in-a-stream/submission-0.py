import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = [] #k size min heap
        self.k = k
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
            return self.min_heap[0]
        
        if self.min_heap[0] < val:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]

            
