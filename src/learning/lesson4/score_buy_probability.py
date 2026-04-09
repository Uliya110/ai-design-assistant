def score_buy_probability(recs: list[dict], clicked_value: int) -> float:
    if clicked_value not in (0, 1):
        raise ValueError("clicked_value must be 0/1")
    subset = [r for r in recs if int(r["clicked"]) == clicked_value]
    if len(subset) == 0:
        raise ValueError("No records for clicked_value")
    bought_count = sum(1 for r in subset if int(r["bought"]) == 1)
    return bought_count / len(subset)

p_buy_click1 = score_buy_probability(records, 1)
p_buy_click0 = score_buy_probability(records, 0)

print("P(buy|click=1) =", p_buy_click1)
print("P(buy|click=0) =", p_buy_click0)
## наивный скоринг. Данные берем из ноутбука урок 4