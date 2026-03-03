import unittest
import os
import pandas as pd
from app.io.input import read_from_file_builtin, read_from_file_pandas

class TestInputFunctions(unittest.TestCase):

    def setUp(self):
        #creating temporary files
        self.test_text_file = "test_temp.txt"
        self.test_csv_file = "test_temp.csv"

        with open(self.test_text_file, 'w', encoding='utf-8') as f:
            f.write("hello world!")

        pd.DataFrame({"A": [1, 2]}).to_csv(self.test_csv_file, index=False)

    def tearDown(self):
        #deleting temporary files
        if os.path.exists(self.test_text_file):
            os.remove(self.test_text_file)
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)

    def test_builtin_reads_correctly(self):
        result = read_from_file_builtin(self.test_text_file)
        self.assertEqual(result, "hello world!")

    def test_builtin_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_builtin("non_existent_file.txt")

    def test_builtin_reads_empty_file(self):
        with open("empty.txt", "w") as f:
            pass
        result = read_from_file_builtin("empty.txt")
        self.assertEqual(result, "")
        os.remove("empty.txt")

    def test_pandas_reads_correctly(self):
        result = read_from_file_pandas(self.test_csv_file)
        self.assertIn("A", result)
        self.assertIn("1", result)

    def test_pandas_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_pandas("non_existent_file.csv")

    def test_pandas_empty_file_error(self):
        with open("empty.csv", "w") as f:
            pass
        with self.assertRaises(pd.errors.EmptyDataError):
            read_from_file_pandas("empty.csv")
        os.remove("empty.csv")

if __name__ == '__main__':
    unittest.main()