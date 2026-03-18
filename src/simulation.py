import random


def queue_success_probability(
    n_tickets_half: int = 100,
    n_trials: int = 10_000,
    seed: int | None = None,
) -> float:
    """Estimate the probability that everyone in a queue gets served.

    Half the people pay with a 50-unit ticket (exact change),
    the other half pay with a 100-unit ticket (requiring 50 change).
    A person with a 100-unit ticket can only be served if the cashier
    has 50-unit change available.

    Args:
        n_tickets_half: Number of 50-unit ticket holders (equal number of 100s).
        n_trials: Monte Carlo iterations.
        seed: Optional random seed for reproducibility.

    Returns:
        Estimated probability that all customers are served successfully.
    """
    if seed is not None:
        random.seed(seed)

    queue = [50] * n_tickets_half + [100] * n_tickets_half
    total = len(queue)
    successes = 0

    for _ in range(n_trials):
        random.shuffle(queue)
        change = 0
        served = 0
        for ticket in queue:
            if ticket == 50:
                change += 1
                served += 1
            elif change > 0:
                change -= 1
                served += 1
            else:
                break
        if served == total:
            successes += 1

    return successes / n_trials
