def sem(values) -> float:
    n = len(values)
    if n <= 0:
        raise ValueError("sem: empty")
    return std_sample(values) / (n ** 0.5)

sem_val = sem(data)
sem_val
## Показывает насколько дрожит среднее значение. Ноутбук урок 5


