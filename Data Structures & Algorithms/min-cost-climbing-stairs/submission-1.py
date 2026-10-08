class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        
        if len(cost) == 1:
            return cost[0]
        
        prev_2 = cost[0]
        prev_1 = cost[1]

        for i in range(2, len(cost)):
            cur = min(prev_2+cost[i], prev_1+cost[i])
            prev_2 = prev_1
            prev_1 = cur
        
        return min(prev_1, prev_2)