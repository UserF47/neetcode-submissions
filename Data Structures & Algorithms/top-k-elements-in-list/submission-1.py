class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = defaultdict(int)

        for num in nums:
            h_map[num] += 1
        
        keys = sorted(h_map, key=h_map.get, reverse=True)

        return keys[:k]