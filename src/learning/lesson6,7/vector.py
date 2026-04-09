import numpy as np

v1 = np.array([16, 44])
v2 = np.array([57, 20])

print("v1 =", v1)
print("v2 =", v2)

assert len(v1) == len(v2) == 2

len_v1 = np.linalg.norm(v1)
len_v2 = np.linalg.norm(v2)

print("Длина v1:", len_v1)
print("Длина v2:", len_v2)

assert len_v1 > 0 and len_v2 > 0

v_sum = v1 + v2
print("Сумма векторов:", v_sum)

dot_value = np.dot(v1, v2)
print("Скалярное произведение:", dot_value)