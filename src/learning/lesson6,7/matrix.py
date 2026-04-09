import numpy as np

X = np.array([
    [16, 22],
    [23, 10],
    [3, 16]
])

print(X)
assert X.shape == (3, 2)

w = np.array([30, 10])
print("Вектор w:", w)

assert len(w) == 2

result = X @ w
print("Результат умножения:", result)

assert len(result) == 3