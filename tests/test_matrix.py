import pytest
from src.matrix import transpose


def test_transpose_1x1():
    assert transpose([[42]]) == [[42]]


def test_transpose_row_vector():
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]


def test_transpose_column_vector():
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]


def test_transpose_square_matrix():
    m = [[1, 2], [3, 4]]
    assert transpose(m) == [[1, 3], [2, 4]]


def test_transpose_rectangular_matrix():
    m = [[1, 2, 3], [4, 5, 6]]
    assert transpose(m) == [[1, 4], [2, 5], [3, 6]]


def test_transpose_twice_is_identity():
    m = [[1, 2, 3], [4, 5, 6]]
    assert transpose(transpose(m)) == m


def test_transpose_empty_matrix():
    assert transpose([]) == []


def test_transpose_row_of_empty():
    assert transpose([[]]) == []
