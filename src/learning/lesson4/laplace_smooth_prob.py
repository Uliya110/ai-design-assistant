def laplace_smooth_prob(successes: int, trials: int) -> float:
    if trials < 0 or successes < 0 or successes > trials:
        raise ValueError("laplace_smooth_prob: invalid counts")
    return (successes + 1) / (trials + 2)

subset0 = [r for r in records if int(r["clicked"]) == 0]
succ0 = sum(1 for r in subset0 if int(r["bought"]) == 1)
p_smooth0 = laplace_smooth_prob(succ0, len(subset0))

print("raw P(buy|click=0) =", p_buy_click0)
print("smooth P(buy|click=0) =", p_smooth0)

## Сглаживание Лапласа. Чтобы избежать нулевых вероятностей. В числитель добавляем 1, в знаменатель 2. Данные берем из ноутбука урок 4