CHECK_LIST = ['Имя', 'Возраст', 'Должность']


def validate_csv_file(file) -> bool:
    if file.endswith('.csv'):
        return True
    return False


def validate_csv_data(data) -> bool:
    "Валидация файла CSV"
    res = data.columns
    if (res != CHECK_LIST).any():
        return False
    return True
