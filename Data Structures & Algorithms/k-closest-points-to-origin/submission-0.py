import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: #total O(nlogn) 
        # size of points is 
        distance_heap = [] # O(k)
        result = [] #O(k)

        for point in points: # total O(nlogk) 
            distance = point[0]**2 + point[1]**2

            if len(distance_heap) < k:
                heapq.heappush(distance_heap, (-distance, point[0], point[1])) 
                continue
                #   -distance bc we want [-5, -4, -1] from heap not -1, as -5 is the largest distance

            largest_distance_point = distance_heap[0]
            largest_distance, point_x, point_y = largest_distance_point

            if distance < -largest_distance: # -5 -> 5
                heapq.heappop(distance_heap)
                heapq.heappush(distance_heap, (-distance, point[0], point[1]))
        
        while distance_heap: # total O(k)
            distance_point = heapq.heappop(distance_heap)
            distance, point_x, point_y = distance_point
            result.append([point_x, point_y])

        return result
