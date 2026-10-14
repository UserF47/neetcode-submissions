class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1] = [res[-1][0], max(intervals[i][1], res[-1][1])]
            else:
                res.append([intervals[i][0], intervals[i][1]])
        
        return res
