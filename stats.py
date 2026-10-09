"""Basic descriptive statistics helpers."""

from collections import Counter


def mean(xs):
    """Return the arithmetic mean of xs. Raises ValueError if xs is empty."""
    if not xs:
        raise ValueError("mean() arg is an empty list")
    return sum(xs) / len(xs)


def median(xs):
    """Return the median of xs. Raises ValueError if xs is empty."""
    if not xs:
        raise ValueError("median() arg is an empty list")
    ordered = sorted(xs)
    n = len(ordered)
    mid = n // 2
    if n % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def mode(xs):
    """Return the most common value in xs, breaking ties by smallest value.

    Raises ValueError if xs is empty.
    """
    if not xs:
        raise ValueError("mode() arg is an empty list")
    counts = Counter(xs)
    highest = max(counts.values())
    candidates = [value for value, count in counts.items() if count == highest]
    return min(candidates)


def variance(xs):
    """Return the population variance of xs. Raises ValueError if xs is empty."""
    if not xs:
        raise ValueError("variance() arg is an empty list")
    avg = mean(xs)
    return sum((x - avg) ** 2 for x in xs) / len(xs)
