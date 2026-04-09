def bayes_posterior(prior: float, likelihood: float, evidence: float) -> float:
    for name, p in [("prior", prior), ("likelihood", likelihood), ("evidence", evidence)]:
        if p < 0 or p > 1:
            raise ValueError(f"bayes_posterior: {name} must be in [0,1]")
    if evidence == 0:
        raise ValueError("bayes_posterior: evidence must be > 0")
    return (likelihood * prior) / evidence

prior = prob_from_counts(counts["count_A"], counts["n"])      # P(bought)
evidence = prob_from_counts(counts["count_B"], counts["n"])   # P(clicked)
likelihood = p_B_given_A                                      # P(clicked|bought)

posterior = bayes_posterior(prior, likelihood, evidence)      # P(bought|clicked)
print("P(bought|clicked) via Bayes =", posterior)
## формула Байеса.Данные берем из ноутбука урок 4