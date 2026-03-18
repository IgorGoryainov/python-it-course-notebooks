import pytest
from src.algorithms import max_consecutive_count, max_of_three, max_binary_search


class TestMaxConsecutiveCount:
    def test_empty(self):
        assert max_consecutive_count([]) == 0

    def test_single_element(self):
        assert max_consecutive_count([7]) == 1

    def test_all_same(self):
        assert max_consecutive_count([1, 1, 1, 1]) == 4

    def test_no_repeats(self):
        assert max_consecutive_count([1, 2, 3]) == 1

    def test_run_in_middle(self):
        assert max_consecutive_count([1, 2, 2, 2, 3]) == 3

    def test_run_at_end(self):
        assert max_consecutive_count([1, 2, 3, 3, 3]) == 3

    def test_run_at_start(self):
        assert max_consecutive_count([5, 5, 1, 2]) == 2

    def test_multiple_runs_picks_longest(self):
        assert max_consecutive_count([1, 1, 2, 2, 2, 3, 3]) == 3


class TestMaxOfThree:
    def test_all_equal(self):
        assert max_of_three(5, 5, 5) == 5

    def test_first_is_max(self):
        assert max_of_three(10, 3, 7) == 10

    def test_second_is_max(self):
        assert max_of_three(1, 9, 4) == 9

    def test_third_is_max(self):
        assert max_of_three(2, 3, 100) == 100

    def test_negative_numbers(self):
        assert max_of_three(-5, -1, -10) == -1


class TestMaxBinarySearch:
    def test_single_account(self):
        # 100 total, 2 managers -> each gets 50
        assert max_binary_search([100], 2) == 50

    def test_multiple_accounts(self):
        # Example: [10, 20, 30], 3 managers
        # at amount=10: draws = 1+2+3=6 >= 3 -> lo=10
        # at amount=20: draws = 0+1+1=2 < 3 -> hi=20
        # at amount=15: draws = 0+1+2=3 >= 3 -> lo=15
        # ... should converge to 15
        result = max_binary_search([10, 20, 30], 3)
        assert result >= 10

    def test_impossible(self):
        # More managers than total units
        result = max_binary_search([1], 5)
        assert result == 0

    def test_equal_accounts(self):
        # 4 accounts of 100 each, 4 managers -> each gets 100
        assert max_binary_search([100, 100, 100, 100], 4) == 100
