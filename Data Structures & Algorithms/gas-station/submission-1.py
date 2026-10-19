class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        len_gas = len(gas)
        cur_gas = 0
        start = 0
        total = 0

        for i in range(len_gas):
            cur_gas += gas[i]
            total += gas[i] - cost[i]

            if cur_gas >= cost[i]:
                cur_gas -= cost[i]
            else:
                cur_gas = 0
                start = i+1
        
        return start if total >= 0 else -1