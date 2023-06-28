import math


class City:
    def __init__(self, identifier: int, x: float, y: float):
        self.identifier = identifier
        self.x = x
        self.y = y

    def calculate_distance(self, other: "City") -> float:
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
