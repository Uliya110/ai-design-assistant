def prob_from_counts(count: int, n: int) -> float:
    if n <= 0:
        raise ValueError("prob_from_counts: n must be > 0")
    if count < 0 or count > n:
        raise ValueError("prob_from_counts: invalid count")
    return count / n

print("P(bought)  =", prob_from_counts(counts["count_A"], counts["n"]))
print("P(clicked) =", prob_from_counts(counts["count_B"], counts["n"]))
## считаем вероятность из частоты