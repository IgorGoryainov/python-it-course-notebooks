import math


def rmse(actual: list, predicted: list) -> float:
    """Root Mean Square Error between two sequences of equal length.

    Args:
        actual: Ground-truth values.
        predicted: Model predictions.

    Returns:
        RMSE as a float.

    Raises:
        ValueError: If sequences have different lengths or are empty.
    """
    if len(actual) != len(predicted):
        raise ValueError("actual and predicted must have the same length")
    if not actual:
        raise ValueError("sequences must not be empty")
    mse = sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual)
    return math.sqrt(mse)
