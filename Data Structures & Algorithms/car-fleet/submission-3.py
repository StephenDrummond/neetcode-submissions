class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ticks = []
        count = 1

        for i in range(len(position)):
            ticks.append((target - position[i]) / speed[i])
        groups = sorted(zip(position, ticks))

        while len(groups) >= 2:
            if groups[-1][1] < groups[-2][1]:
                count += 1
            else:
                groups[-2] = groups[-1]
            groups.pop()

        return count