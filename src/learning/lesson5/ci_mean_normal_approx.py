def ci_mean_normal_approx(values, z: float = 1.96):
    """Приближённый CI для среднего: mean ± z*SEM."""
    m = mean(values)
    se = sem(values)
    return (m - z * se, m + z * se)

ci_norm = ci_mean_normal_approx(data)
ci_norm
## Приближенный 95% CI для среднего. Используется рандомайзер. Ноутбук урок 5


