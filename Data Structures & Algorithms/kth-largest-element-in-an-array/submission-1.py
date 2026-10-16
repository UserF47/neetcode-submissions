import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [] # space: O(k)

        for num in nums: # loop: O(n), heap ops: O(logk), total: O(nlogk)
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                min_num = min_heap[0]
                if min_num < num:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
        
        return min_heap[0]

# nums = [2,3,1,5, 4], k = 2
# min_heap = []

# min_heap = [2]
# min_heap = [2, 3]
# min_heap = [2, 3]
# min_heap = [3, 5]
# min_heap = [4, 5]

# return 4

