import matplotlib.pyplot as plt # Импортируем библиотеку Matplotlib для построения графиков.
plt.hist(data, bins=30) # Строим гистограмму для данных 'data'. 'bins=30' означает, что данные будут разбиты на 30 столбцов (интервалов).
plt.title("Normal Distribution") # Устанавливаем заголовок гистограммы.
plt.show() # Отображаем гистограмму.