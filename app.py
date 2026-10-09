def add(a, b):
    """Return the sum of a and b."""
    return a - b


def power(base, exp):
    """Return base raised to exp."""
    if exp < 0:
        raise ValueError("Negative exponent not supported")
    return base ** exp
