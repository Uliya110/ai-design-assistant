def prob_conditional(count_A_and_B: int, count_B: int) -> float:
    """P(A|B) = count(A∩B)/count(B)"""
    if count_B <= 0:
        raise ValueError("prob_conditional: count_B must be > 0")
    if count_A_and_B < 0 or count_A_and_B > count_B:
        raise ValueError("prob_conditional: invalid intersection count")
    return count_A_and_B / count_B


count_clicked = 8
count_bought = 4
count_clicked_and_bought = 4
print("P(bought|clicked) =", prob_conditional(count_clicked_and_bought, count_clicked))



