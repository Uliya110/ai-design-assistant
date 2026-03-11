from .mean import mean

def variance_sample(values: list[float]) -> float:
    n = len(values)
    if n < 2:
        raise ValueError('variance_sample: need at least 2 values')
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / (n - 1)
