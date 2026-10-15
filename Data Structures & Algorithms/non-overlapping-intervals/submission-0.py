class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals = [[1,2],[2,4],[1,4]] -> [[1,2],[1,4],[2,4]]
        
        # intervals = [1,2], [1,3], [2,3], [3,4]
        # sorted by end time: [1,2], [1,3], [2,3], [3,4]

        intervals.sort(key=lambda x:x[1])
        last_kept_end_time = intervals[0][1]
        kept_non_overlapping_intervals = 1
        
        for i in range(1, len(intervals)):
            # decide if two intervals overlap
            if intervals[i][0] < last_kept_end_time:
                continue # we remove it
            else: # we keep it
                last_kept_end_time = intervals[i][1]
                kept_non_overlapping_intervals += 1
        
        return len(intervals) - kept_non_overlapping_intervals