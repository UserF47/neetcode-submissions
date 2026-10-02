class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.time_map:
            self.time_map[key] = [(timestamp, value)]
        else:
            self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.time_map:
            return ""
        
        time_value = self.time_map[key]
        left = 0
        right = len(time_value) - 1

        while left <= right:
            mid = (left + right) // 2
            if time_value[mid][0] == timestamp:
                return time_value[mid][1]
            
            if time_value[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        if right < 0:
            return ""
        else:
            return time_value[left-1][1]
