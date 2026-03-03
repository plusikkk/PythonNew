from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin

def main():
    # console
    console_text = input_from_console()
    output_to_console(f"Ви ввели: {console_text}")
    write_to_file_builtin("data/output_console.txt", console_text)

    # builtin methods
    builtin_text = read_from_file_builtin("data/text_file.txt")
    output_to_console(f"\nЗчитано з файлу:\n{builtin_text}")
    write_to_file_builtin("data/output_builtin.txt", builtin_text)

    # 3. pandas
    pandas_text = read_from_file_pandas("data/data_file.csv")
    output_to_console(f"\nЗчитано з CSV (pandas):\n{pandas_text}")
    write_to_file_builtin("data/output_pandas.txt", pandas_text)

if __name__ == "__main__":
    main()