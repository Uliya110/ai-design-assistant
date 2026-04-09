import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

url = "https://raw.githubusercontent.com/Uliya110/ai-design-assistant/refs/heads/feature/fix-folder/ai-design-assistant/data/test.csv"

try:
    df = pd.read_csv(url)
    print("Данные успешно загружены из интернета.")
except:
    df = pd.read_csv("your_dataset.csv")
    print("Не удалось загрузить данные из интернета. Используется локальный файл.")

print("Размер таблицы:", df.shape)

df.head()

print("Названия столбцов:")
print(df.columns.tolist())

print("\nТипы данных:")
print(df.dtypes)

print("\nОбщая информация:")
df.info()
print("\nОписательная статистика:")
df.describe()

print("Количество пропусков по столбцам:")
print(df.isna().sum())


grouped = df.groupby("number_customer_service_calls").agg(
    avg_day_minutes=("total_day_minutes", "mean"),
    avg_charge=("total_day_charge", "mean")
)

grouped

correlation = df.corr(numeric_only=True)
correlation

# Средние, максимальные и минимальные значения по нескольким столбцам
df[['total_day_minutes', 'total_eve_minutes', 'total_night_minutes']].agg(['mean', 'max', 'min', 'std'])

# Сортировка по дневным минутам
df_sorted = df.sort_values(by='total_day_minutes', ascending=False)
df_sorted.head(10)  # 10 самых активных клиентов по дневным звонкам


# Топ-5 клиентов с наибольшими дневными минутами
df.nlargest(5, 'total_day_minutes')

# График 1.
plt.figure()
plt.scatter(df["total_day_minutes"], df["total_day_charge"])
plt.xlabel("Дневные минуты")
plt.ylabel("Стоимость")
plt.title("Зависимость стоимости от количества минут")
plt.show()

# График 2.
plt.figure()
plt.hist(df["number_customer_service_calls"])
plt.xlabel("Количество обращений")
plt.ylabel("Частота")
plt.title("Распределение обращений в поддержку")
plt.show()

# График 3.
plt.figure()
plt.bar(grouped.index, grouped["avg_charge"])
plt.xlabel("Количество обращений")
plt.ylabel("Средняя стоимость")
plt.title("Средняя стоимость по количеству обращений")
plt.show()

# Находим клиента с максимальным количеством дневных минут
max_day_idx = df["total_day_minutes"].idxmax()
max_day_minutes = df.loc[max_day_idx, "total_day_minutes"]
max_day_charge = df.loc[max_day_idx, "total_day_charge"]

# Проверка: assert для уверенности
assert max_day_minutes == df["total_day_minutes"].max(), "Ошибка: найденное значение не совпадает с максимумом"

# Среднее количество обращений в поддержку
avg_calls = df["number_customer_service_calls"].mean()
print(f"Среднее количество обращений в поддержку: {avg_calls:.2f}")

# Максимальное количество обращений
max_calls = df["number_customer_service_calls"].max()
print(f"Максимальное количество обращений у одного клиента: {max_calls}")

# Средние международные звонки
avg_intl = df["total_intl_minutes"].mean()
print(f"Среднее количество международных минут: {avg_intl:.2f}")

print("Вывод 1:")
print(f"Есть клиенты с очень высокой активностью. Визуально это подтверждается scatter-графиком стоимости от минут.")

print("\nВывод 2:")
print(f"Гистограмма показала, что большинство клиентов обращаются редко, а редкие выбросы (5–6 раз) помогают выявить «трудных» клиентов.")

print("\nВывод 3:")
print("Международные звонки почти не используются, что видно из описательной статистики и scatter-графиков.")

