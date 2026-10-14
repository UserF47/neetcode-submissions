"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        h = []
        intervals.sort(key=lambda x:x.start)
        room = 0

        for i in range(len(intervals)):
            if not h:
                heapq.heappush(h, intervals[i].end)
                room += 1
            else:
                earliest_end = h[0]

                if earliest_end > intervals[i].start:
                    room += 1
                else:
                    heapq.heappop(h)

                heapq.heappush(h, intervals[i].end)
            
        return room

            
