class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        curr = []
        for i, pos in enumerate(position):
            curr.append((i, pos))
        curr.sort(key=lambda x: x[1], reverse=True)
        time2Target = 0
        fleet = 0
        for i, pos in curr:
            t2t = (target - pos) / speed[i]
            if t2t > time2Target:
                fleet += 1
                time2Target = t2t
        return fleet
        