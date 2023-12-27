import pandas as pd

FILE_PATH = 'csv_files/employees.csv'
CHECK_LIST = ['Имя', 'Возраст', 'Должность']


def avg_age_by_posotion(FILE_PATH) -> dict:
    """Функция по обработке csv файла и
    получению среднего возраста по каждой должности"""
    employee_data = pd.read_csv(
        FILE_PATH,
        encoding='utf-8',
        delimiter=','
    )
    employee_dict = employee_data.groupby(
        'Должность'
    )['Возраст'].mean().to_dict()
    res = employee_data.columns
    if (res != CHECK_LIST).any():
        print(False)

    return employee_dict


result = avg_age_by_posotion(FILE_PATH)
