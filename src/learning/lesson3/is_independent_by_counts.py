def is_independent_by_counts(p_a: float, p_a_given_b: float, tol: float = 0.05) -> bool:
    """Проверка независимости по приближению |P(A|B)-P(A)| <= tol"""
    return abs(p_a_given_b - p_a) <= tol

p_bought = prob_event(count_bought, len(records))
p_bought_given_clicked = prob_conditional(count_clicked_and_bought, count_clicked)


P(clicked) = 0.6666666666666666
P(bought)  = 0.3333333333333333
## нужно подгрузить данные

print("P(bought) =", round(p_bought, 3))
print("P(bought|clicked) =", round(p_bought_given_clicked, 3))
print("independent? ->", is_independent_by_counts(p_bought, p_bought_given_clicked, tol=0.05))


