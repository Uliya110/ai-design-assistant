data_out = np.append(data, 10)
plt.hist(data_out, bins=30) # Строим гистограмму для данных с выбросом 'data_out'.
plt.title("With Outlier") # Устанавливаем заголовок гистограммы, указывающий на наличие выброса.
plt.show() # Отображаем гистограмму.