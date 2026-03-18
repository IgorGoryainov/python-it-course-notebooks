import math
import pytest
from src.geometry import Point


def test_distance_to_same_point():
    p = Point(3, 4)
    assert p.distance_to(p) == 0.0


def test_distance_to_known_values():
    origin = Point(0, 0)
    p = Point(3, 4)
    assert math.isclose(origin.distance_to(p), 5.0)


def test_distance_to_is_symmetric():
    a = Point(1, 2)
    b = Point(4, 6)
    assert math.isclose(a.distance_to(b), b.distance_to(a))


def test_distance_to_negative_coords():
    a = Point(-1, -1)
    b = Point(2, 3)
    assert math.isclose(a.distance_to(b), 5.0)


def test_count_neighbors_none_within_radius():
    center = Point(0, 0)
    far = [Point(100, 100), Point(200, 200)]
    assert center.count_neighbors(far, radius=5.0) == 0


def test_count_neighbors_counts_correctly():
    center = Point(0, 0)
    nearby = [Point(1, 0), Point(0, 1)]
    far = [Point(10, 10)]
    all_points = [center] + nearby + far
    assert center.count_neighbors(all_points, radius=5.0) == 2


def test_count_neighbors_excludes_self():
    p = Point(0, 0)
    assert p.count_neighbors([p], radius=100.0) == 0


def test_str_representation():
    p = Point(3, 7)
    assert str(p) == "(3, 7)"


def test_repr_representation():
    p = Point(1.5, 2.5)
    assert repr(p) == "Point(1.5, 2.5)"
