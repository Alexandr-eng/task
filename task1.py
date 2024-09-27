from datetime import datetime, timedelta

# Исходный массив периодов дат
periods = [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
]

# Функция для разжатия периодов дат
def flatten_periods(periods):
    flattened_dates = []
    for start, end in periods:
        current_date = start
        while current_date <= end:
            flattened_dates.append(current_date)
            current_date += timedelta(days=1)
    return flattened_dates

# Разжатие периодов дат
flattened_dates = flatten_periods(periods)

# Вывод результата
for date in flattened_dates:
    print(date)