from collections import deque


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        queue = deque()
        queue.append((0, 0))
        result = set()
        while queue:
            remain_x, remain_y = queue.popleft()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True

            if (remain_x, remain_y) in result:
                continue
            result.add((remain_x, remain_y))

            queue.append((x, remain_y))
            queue.append((0, remain_y))

            queue.append((remain_x, y))
            queue.append((remain_x, 0))

            move = min(remain_x, y - remain_y)
            queue.append((remain_x - move, remain_y + move))
            move = min(remain_y, x - remain_x)
            queue.append((remain_x + move, remain_y - move))

        return False




