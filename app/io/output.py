def output_to_console(text):
    """
    Виводить переданий текст у консоль.

    Args:
        text (str): Текст для виводу.
    """
    print(text)

def write_to_file_builtin(filepath, text):
    """
    Записує переданий текст у файл за допомогою вбудованих можливостей Python.

    Args:
        filepath (str): Шлях до файлу, куди буде записано текст.
        text (str): Текст для запису.
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)