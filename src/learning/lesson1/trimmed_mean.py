from .mean import mean

def trimmed_mean(values: list[float], k: int = 1) -> float:
    n = len(values)
    if n == 0:
        raise ValueError('trimmed_mean: empty list')
    if 2 * k >= n:
        raise ValueError('trimmed_mean: k too large')
    s = sorted(values)
    core = s[k:n - k]
    return mean(core)
