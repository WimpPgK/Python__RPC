import unittest
from ResultsDataBase import ResultsDataBase

class TestClient(unittest.TestCase):

    def test_sqlite(self):
        resultsDataBase = ResultsDataBase()
        rows = resultsDataBase.select_all_results()
        table_size_before = len(rows)
        resultsDataBase.main()

        rows = resultsDataBase.select_all_results()
        table_size_after = len(rows)
        self.assertEqual(table_size_before + 1, table_size_after)

if __name__ == '__main__':
    unittest.main()
