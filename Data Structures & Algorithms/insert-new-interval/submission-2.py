class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        
        res.append(newInterval)

        while i < len(intervals) and res[-1][1] >= intervals[i][0]:
            res[-1] = [min(intervals[i][0], res[-1][0]), max(intervals[i][1], res[-1][1])]
            i += 1
        
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res
