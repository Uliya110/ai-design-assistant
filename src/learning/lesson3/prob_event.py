def prob_event(count_A: int, n: int) -> float:
    """P(A) = count(A)/n"""
    if n <= 0:
        raise ValueError("prob_event: n must be > 0")
    if count_A < 0 or count_A > n:
        raise ValueError("prob_event: invalid count")
    return count_A / n



records = [
    {"clicked": 1, "bought": 1},
    {"clicked": 1, "bought": 0},
    {"clicked": 1, "bought": 1},
    {"clicked": 0, "bought": 0},
    {"clicked": 1, "bought": 0},
    {"clicked": 0, "bought": 0},
    {"clicked": 1, "bought": 1},
    {"clicked": 0, "bought": 0},
    {"clicked": 1, "bought": 0},
    {"clicked": 1, "bought": 1},
    {"clicked": 0, "bought": 0},
    {"clicked": 1, "bought": 0},
]
n = len(records)

count_clicked = 8
count_bought = 4
count_clicked_and_bought = 4

print("P(clicked) =", prob_event(count_clicked, n))
print("P(bought)  =", prob_event(count_bought, n))