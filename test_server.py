import unittest
from module_4_server import Module3Server
from dbmanager import DbManager

server = Module3Server()
db = DbManager('localhost', 'root', '', 'testowa')

class TestServer(unittest.TestCase):
    def test_create_table(self):
        server.exposed_create_table()

    def test_save_code(self):
        query = "SELECT * FROM programs"
        db.executesql(query)
        rows = db.get_result()
        table_size_before = len(rows)

        content = ''
        with open('code.txt', 'r') as file:
            content = file.readlines()

        server.exposed_save_code(content)

        db.executesql(query)
        rows = db.get_result()
        table_size_after = len(rows)
        self.assertEqual(table_size_before + 1, table_size_after)
        

    def test_execute_code(self):
        fib = server.exposed_execute_code(8)
        self.assertEqual(fib, 21)

    def test_compare_code(self):
        query = "SELECT * FROM programs_diffs"
        db.executesql(query)
        rows = db.get_result()
        table_size_before = len(rows)
        first_row_match = rows[0]['similarity']

        server.exposed_compare_code(11)

        db.executesql(query)
        rows = db.get_result()
        table_size_after = len(rows)
        last_row_match = rows[len(rows) - 1]['similarity']
        self.assertEqual(table_size_before + 1, table_size_after)
        self.assertEqual(first_row_match, last_row_match)

if __name__ == '__main__':
    unittest.main()