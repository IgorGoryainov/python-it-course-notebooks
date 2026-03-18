import math


class Point:
    """A 2D point with distance and neighborhood utilities."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def count_neighbors(self, points: list, radius: float = 5.0) -> int:
        return sum(1 for p in points if p is not self and self.distance_to(p) < radius)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
