import numpy as np

rng = np.random.default_rng(42)
data = rng.normal(loc=10.0, scale=2.0, size=50)
## Используем генератор случайных чисел и нормальное распределение. Ноутбук урок 5


def mean(values) -> float:
    """Среднее арифметическое для списка/массива."""
    if len(values) == 0:
        raise ValueError("mean: empty")
    return float(sum(values)) / len(values)

m = mean(data)
m
