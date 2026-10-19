class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_intervals = {}

        for i in range(len(s)):
            if s[i] in letter_intervals:
                letter_intervals[s[i]][1] = i
            else:
                letter_intervals[s[i]] = [i, i]
        
        intervals = list(letter_intervals.values())
        intervals.sort(key=lambda x:x[0])

        latest_interval = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if intervals[i][0] < latest_interval[1]:
                latest_interval = [latest_interval[0], max(latest_interval[1], intervals[i][1])]
            else:
                res.append(latest_interval[1] - latest_interval[0] + 1)
                latest_interval = intervals[i]
        
        res.append(latest_interval[1] - latest_interval[0] + 1)
        
        return res
