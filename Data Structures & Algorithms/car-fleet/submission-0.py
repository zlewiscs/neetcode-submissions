class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]

        stack  = []

        pairs.sort(reverse=True)
        fleet = 1

        prev_time = (target - pairs[0][0]) / pairs[0][1] # distance / speed

        for i in range(1, len(pairs)):
            current_car = pairs[i]
            current_time = (target - current_car[0]) / current_car[1]

            if current_time > prev_time:
                fleet += 1
                prev_time = current_time
        
        return fleet

