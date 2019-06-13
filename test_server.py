import unittest
from module_4_server import Module4Server
from dbmanager import DbManager

server = Module4Server()
db = DbManager('localhost', 'root', '', 'testowa')

class TestServer(unittest.TestCase):
    def test_create_table(self):
        server.exposed_create_table()

    def test_save_code(self):
        query = "SELECT COUNT(*) FROM programs"
        db.executesql(query)
        rows = db.get_result()
        db.commit_changes()
        table_size_before = rows[0]['COUNT(*)']

        content = ''
        with open('code.txt', 'r') as file:
            content = file.readlines()

        server.exposed_save_code(content)

        db.executesql(query)
        rows = db.get_result()
        db.commit_changes()
        table_size_after = rows[0]['COUNT(*)']
        self.assertEqual(table_size_before + 1, table_size_after)      

    def test_execute_code(self):
        fib = server.exposed_execute_code(8)
        self.assertEqual(fib, 21)

    def test_compare_code(self):
        server.exposed_compare_code(68)

if __name__ == '__main__':
    unittest.main()