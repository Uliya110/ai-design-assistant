def build_binary_counts(recs: list[dict], a_key: str, b_key: str) -> dict:
    n = len(recs)
    count_A = 0
    count_B = 0
    count_A_and_B = 0

    for r in recs:
        a = int(r[a_key])
        b = int(r[b_key])
        if a not in (0, 1) or b not in (0, 1):
            raise ValueError("build_binary_counts: values must be 0/1")
        if a == 1:
            count_A += 1
        if b == 1:
            count_B += 1
        if a == 1 and b == 1:
            count_A_and_B += 1

    return {"n": n, "count_A": count_A, "count_B": count_B, "count_A_and_B": count_A_and_B}

counts = build_binary_counts(records, "bought", "clicked")
counts
## Счетчик частоты для Байеса. При условии, что есть кортеж records = [{}] ниже идет
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