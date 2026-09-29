class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleet = 0
        time_front_car = 0

        for p, s in cars:
            t = (target-p) / s

            if t > time_front_car:
                fleet += 1
                time_front_car = t
            
        
        return fleet
  