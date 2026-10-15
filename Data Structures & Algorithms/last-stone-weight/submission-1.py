import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_weights = [-weight for weight in stones]
        heapq.heapify(negative_weights)

        while len(negative_weights) > 1:
            largest_weight = heapq.heappop(negative_weights)
            second_largest_weight = heapq.heappop(negative_weights)

            difference = -abs(largest_weight - second_largest_weight)

            if difference != 0:
                heapq.heappush(negative_weights, difference)
        
        return -negative_weights[0] if negative_weights else 0
        