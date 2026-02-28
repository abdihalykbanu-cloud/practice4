# dates.py

from datetime import datetime, timedelta

# Получить текущую дату и время
def get_current_datetime():
    return datetime.now()


# Добавить дни к дате
def add_days_to_date(days):
    return datetime.now() + timedelta(days=days)


# Разница между двумя датами (в днях)
def date_difference(d1, d2):
    diff = d2 - d1
    return diff.days