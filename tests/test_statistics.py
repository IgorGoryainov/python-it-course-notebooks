import math
import pytest
from src.statistics import rmse


def test_rmse_perfect_prediction():
    assert rmse([1, 2, 3], [1, 2, 3]) == 0.0


def test_rmse_known_value():
    actual = [0, 0, 0, 0]
    predicted = [2, 2, 2, 2]
    assert math.isclose(rmse(actual, predicted), 2.0)


def test_rmse_single_element():
    assert math.isclose(rmse([5.0], [2.0]), 3.0)


def test_rmse_float_values():
    actual = [1.0, 2.0, 3.0]
    predicted = [1.5, 2.5, 3.5]
    expected = math.sqrt(0.25)
    assert math.isclose(rmse(actual, predicted), expected)


def test_rmse_is_nonnegative():
    assert rmse([10, 20], [5, 15]) >= 0


def test_rmse_different_lengths_raises():
    with pytest.raises(ValueError, match="same length"):
        rmse([1, 2, 3], [1, 2])


def test_rmse_empty_raises():
    with pytest.raises(ValueError, match="empty"):
        rmse([], [])
