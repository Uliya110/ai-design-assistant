def bootstrap_ci_mean(values, n_boot: int = 2000, alpha: float = 0.05, seed: int = 0):
    means = bootstrap_means(values, n_boot=n_boot, seed=seed)
    low = float(np.quantile(means, alpha/2))
    high = float(np.quantile(means, 1 - alpha/2))
    return low, high

ci_boot = bootstrap_ci_mean(data, n_boot=2000, alpha=0.05, seed=1)
ci_boot
## Бутстрэп CI через квантили 2,5% и 97,5%. Используется рандомайзер. Ноутбук урок 5


