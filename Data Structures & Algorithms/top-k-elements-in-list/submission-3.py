class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        bucket = [[] for _ in range(len(nums) + 1)]

        h_map = defaultdict(int)

        for num in nums:
            h_map[num] += 1

        for key, v in h_map.items():
            bucket[v].append(key)
        
        counter = k
        for i in range(len(nums), 0, -1):
            if len(bucket[i]) != 0:
                for num in bucket[i]:
                    res.append(num)
                    counter -= 1
                if counter == 0:
                    return res