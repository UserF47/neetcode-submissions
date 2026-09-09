class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        gate = deque()
        step = 1

        rows = len(rooms)
        cols = len(rooms[0])

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    gate.append((i, j))
        
        while gate:
            next_round_gate = deque()

            while gate:
                i, j = gate.popleft()

                if i-1>=0 and rooms[i-1][j] == 2147483647:
                    rooms[i-1][j] = step
                    next_round_gate.append((i-1, j))
                
                if i+1<rows and rooms[i+1][j] == 2147483647:
                    rooms[i+1][j] = step
                    next_round_gate.append((i+1, j))
            
                if j-1>=0 and rooms[i][j-1] == 2147483647:
                    rooms[i][j-1] = step
                    next_round_gate.append((i, j-1))
                
                if j+1<cols and rooms[i][j+1] == 2147483647:
                    rooms[i][j+1] = step
                    next_round_gate.append((i, j+1))
                        
            step += 1

            while next_round_gate:
                gate.append(next_round_gate.popleft())
        
        # return rooms