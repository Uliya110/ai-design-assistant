import pandas as pd
import matplotlib.pyplot as plt
import re
from IPython.display import display

url = "https://raw.githubusercontent.com/Uliya110/ai-design-assistant/refs/heads/feature/fix-folder/ai-design-assistant/data/dataset_cleaned_reviews.csv"

try:
    df = pd.read_csv(url)
    print("Данные успешно загружены из интернета.")
except:
    df = pd.read_csv("your_dataset.csv")
    print("Не удалось загрузить данные из интернета. Используется локальный файл.")

print("Размер таблицы:", df.shape)

df.head()

# Словарь с переводом столбцов
column_names_russian = {
    'cleaned_review': 'Текст отзыва',
    'sentiments': 'Тональность',
    'review_score': 'Оценка',
    'cleaned_review_length': 'Длина текста в символах'
}

print("Названия столбцов:")
print(df.columns.tolist())

print("\nТипы данных:")
print(df.dtypes)

print("\nКоличество пропусков:")
print(df.isna().sum())

print("\nДоступ к конкретной строке:")
print(df.iloc[0])

print("\nСправочник столбцов Amazon:")
for col, name in column_names_russian.items():
    print(f"{col} -> {name}")

# Проверка наличия обязательного столбца 'cleaned_review'
if 'cleaned_review' not in df.columns:
    raise ValueError(f"Столбец с текстом не найден. Доступные столбцы: {df.columns.tolist()}")

# Длина текста в символах
s_length = df['cleaned_review'].str.len()
df['text_length_chars'] = s_length
print("\nДлина текста в символах (первые 5 строк):")
print(df['text_length_chars'].head())

# Количество слов в отзыве
word_count = df['cleaned_review'].str.split().str.len()
df['word_count'] = word_count
print("\nКоличество слов в отзыве (первые 5 строк):")
print(df['word_count'].head())

# Замена тональности через map
sentiments_text = df['sentiments'].map({
    'positive': 'Положительный',
    'negative': 'Отрицательный',
    'neutral': 'Нейтральный'
})
df['sentiments_text'] = sentiments_text
print("\nТональность после map (первые 5 строк):")
print(df['sentiments_text'].head())

# Создание словаря — портрет отзыва
df['review_profile'] = df.apply(lambda row: {
    'Тональность': row['sentiments_text'],
    'Оценка': row['review_score'],
    'Длина_символов': row['text_length_chars'],
    'Количество_слов': row['word_count']
}, axis=1)
print("\nПортрет отзыва (первые 3 строки):")
print(df['review_profile'].head(3))


sentiment_counts = df['sentiments'].value_counts()
print("\nРаспределение тональности:")
print(sentiment_counts)

# Описательная статистика
print(df.describe())

# Средняя оценка по тональности
mean_scores = df.groupby('sentiments')['review_score'].mean()
print("\nСредняя оценка по тональности:")
print(mean_scores)

# Гистограмма тональности
plt.figure()
sentiment_counts.plot(kind='bar')
plt.title('Распределение тональности отзывов')
plt.xlabel('Тональность')
plt.ylabel('Количество')
plt.show()

# Гистограмма оценок
plt.figure()
df['review_score'].plot(kind='hist', bins=5)
plt.title('Распределение оценок')
plt.xlabel('Оценка')
plt.ylabel('Частота')
plt.show()

# Просмотр первых 10 строк тональности и оценок
sample_check = df[['sentiments', 'review_score']].head(10)
print(sample_check)

# Дополнительные функции
columns_list = df.columns.tolist()
dtypes_info = df.dtypes
missing_values = df.isna().sum()
specific_row = df.iloc[5]

print("\nСписок столбцов:", columns_list)
print("\nТипы данных:\n", dtypes_info)
print("\nПропущенные значения:\n", missing_values)
print("\nСтрока 6:\n", specific_row)

# Assert — проверка корректности данных
assert 'cleaned_review' in df.columns, 'Столбец с текстом отсутствует!'
assert df['review_score'].min() >= 1 and df['review_score'].max() <= 5, 'Оценки выходят за допустимый диапазон'
assert set(df['sentiments'].unique()).issubset({'positive', 'negative', 'neutral'}), 'Присутствуют неожиданные значения тональности'


