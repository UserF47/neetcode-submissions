class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.time_map:
            return ""
        else:
            vals = self.time_map[key]
            left = 0
            right = len(vals) - 1

            while left <= right:
                mid = (left + right) // 2
                if vals[mid][1] == timestamp:
                    return vals[mid][0]

                if vals[mid][1] < timestamp:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return vals[right][0] if right >= 0 else ""
