import pandas as pd

def input_from_console():
    """
    Зчитує текст, введений користувачем з консолі.

    Returns:
        str: Введений користувачем текст.
    """
    return input("Будь ласка, введіть якийсь текст: ")


def read_from_file_builtin(filepath):
    """
    Зчитує вміст файлу за допомогою вбудованих можливостей Python.

    Args:
        filepath (str): Шлях до файлу.

    Returns:
        str: Вміст файлу у вигляді рядка.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def read_from_file_pandas(filepath):
    """
    Зчитує дані з файлу (наприклад, CSV) за допомогою бібліотеки pandas.

    Args:
        filepath (str): Шлях до файлу.

    Returns:
        str: Зчитані дані у текстовому форматі.
    """
    dataframe = pd.read_csv(filepath)
    return dataframe.to_string()