import pytest
from src.simulation import queue_success_probability


def test_returns_probability_between_0_and_1():
    prob = queue_success_probability(n_tickets_half=10, n_trials=500, seed=42)
    assert 0.0 <= prob <= 1.0


def test_result_is_reproducible_with_seed():
    p1 = queue_success_probability(n_tickets_half=50, n_trials=1000, seed=99)
    p2 = queue_success_probability(n_tickets_half=50, n_trials=1000, seed=99)
    assert p1 == p2


def test_probability_matches_catalan_formula():
    # For n equal-split tickets, P(success) ≈ 1/(n+1) (Catalan number result).
    # With n=100: expected ≈ 1/101 ≈ 0.0099
    prob = queue_success_probability(n_tickets_half=100, n_trials=20_000, seed=0)
    assert 0.006 <= prob <= 0.015


def test_small_queue_probability():
    # n=1: one 50-ticket and one 100-ticket. Success iff 50 comes first -> P = 0.5
    prob = queue_success_probability(n_tickets_half=1, n_trials=5000, seed=7)
    assert 0.4 <= prob <= 0.6
