def transpose(matrix: list) -> list:
    """Transpose a 2D list (matrix).

    Args:
        matrix: A non-empty list of rows, each row having equal length.

    Returns:
        Transposed matrix as a list of lists.
    """
    if not matrix or not matrix[0]:
        return []
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]
