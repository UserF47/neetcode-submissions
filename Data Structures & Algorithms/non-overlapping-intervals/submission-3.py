class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        res = 0
        last_interval = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] < last_interval[1]:
                if intervals[i][1] < last_interval[1]:
                    last_interval = intervals[i]

                res += 1
            else:
                last_interval = intervals[i]
        
        return res
                