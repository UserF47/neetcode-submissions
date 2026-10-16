import heapq

class MedianFinder:

    def __init__(self):
        self.lower_heap = [] #max heap, top = max value, keep negated value of the integers we add
        self.upper_heap = [] #min heap, top = min value, keep actual value of the integers we add

    def addNum(self, num: int) -> None: # O(logn)
        if not self.lower_heap:
            heapq.heappush(self.lower_heap, -num) # keep negated value of the integers we add
        else:
            # compare top of lower_heap
            neg_max_from_lower_heap = -self.lower_heap[0]

            if num >= neg_max_from_lower_heap:
                heapq.heappush(self.upper_heap, num)
            else:
                heapq.heappush(self.lower_heap, -num)

            # check if two heaps are balanced, size off by less than 2
            size_lower_heap = len(self.lower_heap)
            size_upper_heap = len(self.upper_heap)
            if size_lower_heap - size_upper_heap == 2:
                top_lower_heap = heapq.heappop(self.lower_heap)
                heapq.heappush(self.upper_heap, -top_lower_heap) # -top_lower_heap to convert it back
            
            if size_upper_heap - size_lower_heap== 2:
                top_upper_heap = heapq.heappop(self.upper_heap)
                heapq.heappush(self.lower_heap, -top_upper_heap) 
                # -top_upper_heap to convert it to its negated form


    def findMedian(self) -> float: #O(logn)
        if not self.upper_heap: # only one integer added
            return -self.lower_heap[0]

        size_lower_heap = len(self.lower_heap)
        size_upper_heap = len(self.upper_heap)

        top_lower_heap = self.lower_heap[0]
        top_upper_heap = self.upper_heap[0]

        #if even size
        if size_lower_heap == size_upper_heap:
            return (-top_lower_heap + top_upper_heap) / 2
        
        if size_lower_heap > size_upper_heap:
            return -self.lower_heap[0]
        
        if size_lower_heap < size_upper_heap:
            return self.upper_heap[0]

