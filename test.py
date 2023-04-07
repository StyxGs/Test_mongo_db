import pandas as pd

# создаем список дат
date_list = pd.date_range(start="2022-10-01T00:00:00", end="2022-11-30T23:59:00", freq='M')

t = pd.to_datetime(date_list)
data = pd.DataFrame({'data': t})

# группируем список дат по часам
grouped_dates = data.groupby(pd.Grouper(freq='H', key='data'))

# выводим результат
for key, group in grouped_dates:
    print(key)
