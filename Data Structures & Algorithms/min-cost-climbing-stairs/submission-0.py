class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_2 = cost[0]
        prev_1 = cost[1]
        cur = 0

        for i in range(2, len(cost)):
            cur = min(prev_2, prev_1) + cost[i]
            prev_2 = prev_1
            prev_1 = cur

        return min(prev_1, prev_2)