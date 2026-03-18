def max_consecutive_count(sequence: list) -> int:
    """Return the length of the longest run of equal consecutive elements.

    Examples:
        [1, 1, 1, 2, 3] -> 3
        [1, 2, 3] -> 1
        [] -> 0
    """
    if not sequence:
        return 0
    max_count = 1
    current_count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1
    return max_count


def max_of_three(a: float, b: float, c: float) -> float:
    """Return the largest of three values."""
    return max(a, b, c)


def max_binary_search(accounts: list, managers: int) -> int:
    """Find the maximum equal disbursement each manager can receive.

    Each manager gets floor(account_balance / amount) draws.
    Find the largest `amount` such that the total draws >= managers.

    Args:
        accounts: List of account balances (positive integers).
        managers: Number of managers to serve.

    Returns:
        Maximum disbursement per manager, or 0 if impossible.
    """
    import math

    accounts = sorted(accounts)
    lo, hi = 0, sum(accounts)

    while hi - lo > 1:
        mid = math.floor((hi + lo) / 2)
        if mid == 0:
            break
        total_draws = sum(math.floor(a / mid) for a in accounts)
        if total_draws < managers:
            hi = mid
        else:
            lo = mid

    return lo
